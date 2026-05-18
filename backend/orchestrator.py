import asyncio
from typing import Optional
from library.engine import retrieve
from thinker.engine import generate_answer_stream
from speaker.engine import synthesize_pcm_stream
from shared.text import split_for_tts, get_filler
from shared.metrics import TurnMetrics, log_turn

# Global state to track turn ownership
active_turn_id: Optional[str] = None

def detect_text_language(text: str, default_lang: str) -> str:
    # Check for Devanagari range (U+0900 to U+097F) - represents Hindi/Hinglish text
    if any('\u0900' <= char <= '\u097F' for char in text):
        return "hi"
    # Check for Gujarati range (U+0A80 to U+0AFF) - represents Gujarati text
    if any('\u0A80' <= char <= '\u0AFF' for char in text):
        return "gu"
    # If there is no Hindi or Gujarati characters, but there are Latin letters, it must be English
    if any('a' <= char.lower() <= 'z' for char in text):
        return "en"
    return default_lang

async def run_pipeline(
    text: str,
    lang: str,
    turn_id: str,
    history: list[dict],
    ws_send_bytes,
    ws_send_json,
    initial_chunks: list[str] = None
):
    global active_turn_id
    active_turn_id = turn_id
    metrics = TurnMetrics(turn_id=turn_id)
    start_time = asyncio.get_event_loop().time()

    # ── Helper: stale check ───────────────────────────────────────────
    def is_stale() -> bool:
        return turn_id != active_turn_id

    # 0. Instant Farewell Fast-Exit ───────────────────────────────────
    farewells = [
        "bye", "goodbye", "alvida", "khuda hafiz",
        "phari malishu", "shubh ratri", "theek hai bye", "bas theek hai bye",
    ]
    clean_text = text.lower().strip().replace(".", "").replace("!", "")
    if any(f in clean_text for f in farewells):
        if lang == "hi":
            farewell_msg = "जी, बिल्कुल। अपना ख्याल रखिये, गुडबाय!"
        elif lang == "gu":
            farewell_msg = "જી, ચોક્કસ. તમારી સંભાળ રાખો, ગુડ-બાય!"
        else:
            farewell_msg = "Goodbye! Have a great day."
        await ws_send_json({"type": "tts_start", "turn_id": turn_id})
        async for pcm in synthesize_pcm_stream(farewell_msg, lang, check_stale=is_stale):
            if is_stale():
                await ws_send_json({"type": "tts_end", "turn_id": turn_id})
                return
            if pcm:
                await ws_send_bytes(pcm)
        await ws_send_json({"type": "tts_end", "turn_id": turn_id})
        metrics.total_turn_ms = int((asyncio.get_event_loop().time() - start_time) * 1000)
        log_turn(metrics)
        return farewell_msg

    # 1. Kick off RAG retrieval in background immediately ──────────────
    retrieval_task = None
    if not initial_chunks:
        retrieval_task = asyncio.create_task(asyncio.to_thread(retrieve, text))

    # 2. Speak filler instantly to mask latency ───────────────────────
    # Check turn_id on EVERY PCM chunk so barge-in kills filler mid-word.
    tts_started = False  # Track if tts_start was signaled (shared across filler & main response)
    if not (initial_chunks and "GREETING_BYPASS_RAG" in initial_chunks):
        filler = get_filler(lang)
        filler_start = asyncio.get_event_loop().time()
        async for pcm in synthesize_pcm_stream(filler, lang, check_stale=is_stale):
            if is_stale():
                # Interrupted during filler — cancel background retrieval immediately
                if retrieval_task:
                    retrieval_task.cancel()
                if tts_started:
                    await ws_send_json({"type": "tts_end", "turn_id": turn_id})
                metrics.stale_response = True
                return
            if pcm:
                if not tts_started:
                    tts_started = True
                    await ws_send_json({"type": "tts_start", "turn_id": turn_id})
                await ws_send_bytes(pcm)
                if metrics.filler_ms == 0:
                    metrics.filler_ms = int((asyncio.get_event_loop().time() - filler_start) * 1000)

    # 3. Await retrieval (or use pre-cached speculative chunks) ────────
    retrieval_start = asyncio.get_event_loop().time()
    if retrieval_task:
        try:
            # Poll done state every 20ms to allow instant interrupt mid-RAG
            while not retrieval_task.done():
                if is_stale():
                    retrieval_task.cancel()
                    if tts_started:
                        await ws_send_json({"type": "tts_end", "turn_id": turn_id})
                    return
                await asyncio.sleep(0.02)
            chunks = await retrieval_task
        except asyncio.CancelledError:
            return
    else:
        chunks = initial_chunks
    metrics.retrieval_ms = int((asyncio.get_event_loop().time() - retrieval_start) * 1000)

    if is_stale():
        if tts_started:
            await ws_send_json({"type": "tts_end", "turn_id": turn_id})
        return

    # 4. Stream LLM tokens + TTS in a tight interleaved pipeline ──────
    full_answer = ""
    token_buffer = ""
    llm_start = asyncio.get_event_loop().time()

    async for token in generate_answer_stream(text, chunks, lang, history):
        if is_stale():
            # Interrupted mid-generation — cleanly close the TTS frame
            if tts_started:
                await ws_send_json({"type": "tts_end", "turn_id": turn_id})
            return

        if metrics.llm_first_token_ms == 0:
            metrics.llm_first_token_ms = int((asyncio.get_event_loop().time() - llm_start) * 1000)

        full_answer += token
        token_buffer += token

        # Phrase-level chunking — speak each natural phrase as it completes
        phrases = split_for_tts(token_buffer)
        if len(phrases) > 1:
            to_speak = phrases[0]
            token_buffer = "".join(phrases[1:])

            phrase_lang = detect_text_language(to_speak, lang)
            async for pcm in synthesize_pcm_stream(to_speak, phrase_lang, check_stale=is_stale):
                if is_stale():
                    if tts_started:
                        await ws_send_json({"type": "tts_end", "turn_id": turn_id})
                    return
                if pcm:
                    # Lazy tts_start: fire the signal only when first audio byte is ready
                    # so the frontend never transitions to "speaking" before sound starts
                    if not tts_started:
                        tts_started = True
                        await ws_send_json({"type": "tts_start", "turn_id": turn_id})
                    if metrics.tts_first_audio_ms == 0:
                        metrics.tts_first_audio_ms = int((asyncio.get_event_loop().time() - llm_start) * 1000)
                    await ws_send_bytes(pcm)

    # Speak any remaining buffered tokens
    if token_buffer.strip() and not is_stale():
        phrase_lang = detect_text_language(token_buffer, lang)
        async for pcm in synthesize_pcm_stream(token_buffer, phrase_lang, check_stale=is_stale):
            if is_stale():
                if tts_started:
                    await ws_send_json({"type": "tts_end", "turn_id": turn_id})
                return
            if pcm:
                if not tts_started:
                    tts_started = True
                    await ws_send_json({"type": "tts_start", "turn_id": turn_id})
                await ws_send_bytes(pcm)

    if tts_started and not is_stale():
        await ws_send_json({"type": "tts_end", "turn_id": turn_id})

    metrics.total_turn_ms = int((asyncio.get_event_loop().time() - start_time) * 1000)
    log_turn(metrics)

    return full_answer
