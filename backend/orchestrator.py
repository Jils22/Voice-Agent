import asyncio
from typing import AsyncGenerator, Optional
from library.engine import retrieve
from thinker.engine import generate_answer_stream
from speaker.engine import synthesize_pcm_stream
from shared.text import split_for_tts, get_filler
from shared.metrics import TurnMetrics, log_turn

# Global state to track turn ownership
active_turn_id: Optional[str] = None

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
    
    # Proactively clear client-side playback queue to instantly stop any running/queued previous responses
    await ws_send_json({"type": "clear_queue"})
    await ws_send_json({"type": "tts_start", "turn_id": turn_id})
    
    active_turn_id = turn_id
    metrics = TurnMetrics(turn_id=turn_id)
    start_time = asyncio.get_event_loop().time()

    # 0. Check for Instant Farewell (Principle: Fast Exit)
    farewells = [
        "bye", "goodbye", "chalo bye",
        "alvida", "khuda hafiz", "fir milenge", "phari malishu", "shubh ratri", "theek hai bye", "bas theek hai bye",
        "dhanyavad", "dhanyawaad", "धन्यवाद", "shukriya", "शुक्रिया", "thanks", "thank you", "thnx",
        "aavjo", "avjo", "આવજો",
        "bas itna hi", "bas", "bas itnu j", "बस", "બસ",
        "aatlu j chhe", "aatlu j", "આટલું જ છે", "આટલું જ"
    ]
    clean_text = text.lower().strip().replace(".", "").replace("!", "").replace(",", "").replace("?", "")
    if any(f in clean_text for f in farewells):
        if "gu" in lang.lower():
            farewell_msg = "તમારો ખૂબ ખૂબ આભાર! પોતાનું ધ્યાન રાખજો, આવજો!"
        elif "hi" in lang.lower():
            farewell_msg = "जी, बिल्कुल। आपका बहुत-बहुत धन्यवाद! अपना ख्याल रखिएगा, अलविदा!"
        else:
            farewell_msg = "You are very welcome! Take care and have a great day. Goodbye!"

        async for pcm in synthesize_pcm_stream(farewell_msg, lang):
            if pcm:
                await ws_send_bytes(pcm)
        await ws_send_json({"type": "tts_end", "turn_id": turn_id})
        metrics.total_turn_ms = int((asyncio.get_event_loop().time() - start_time) * 1000)
        log_turn(metrics)
        return farewell_msg

    # 1. Start RAG in background if not already provided (Principle 3)
    if not initial_chunks:
        retrieval_task = asyncio.create_task(asyncio.to_thread(retrieve, text))
    else:
        retrieval_task = None

    # 2. Speak filler immediately (Principle 5)
    # Skip filler for greetings to be more professional
    if not (initial_chunks and "GREETING_BYPASS_RAG" in initial_chunks):
        filler = get_filler(lang)
        filler_start = asyncio.get_event_loop().time()
        async for pcm in synthesize_pcm_stream(filler, lang):
            if turn_id != active_turn_id:
                metrics.stale_response = True
                return
            if pcm:
                await ws_send_bytes(pcm)
                if metrics.filler_ms == 0:
                    metrics.filler_ms = int((asyncio.get_event_loop().time() - filler_start) * 1000)

    # 3. Wait for retrieval (or use speculative chunks)
    retrieval_start = asyncio.get_event_loop().time()
    if retrieval_task:
        chunks = await retrieval_task
    else:
        chunks = initial_chunks
    metrics.retrieval_ms = int((asyncio.get_event_loop().time() - retrieval_start) * 1000)

    if turn_id != active_turn_id:
        return

    # 4. Stream LLM + TTS (Principle 4)
    full_answer = ""
    token_buffer = ""
    llm_start = asyncio.get_event_loop().time()

    async for token in generate_answer_stream(text, chunks, lang, history):
        if turn_id != active_turn_id:
            return
        
        if metrics.llm_first_token_ms == 0:
            metrics.llm_first_token_ms = int((asyncio.get_event_loop().time() - llm_start) * 1000)

        full_answer += token
        token_buffer += token

        # Phrase-level chunking
        phrases = split_for_tts(token_buffer)
        if len(phrases) > 1:
            # We have a complete phrase (the last element is the remaining buffer)
            to_speak = phrases[0]
            token_buffer = "".join(phrases[1:])

            async for pcm in synthesize_pcm_stream(to_speak, lang):
                if turn_id != active_turn_id:
                    return
                if metrics.tts_first_audio_ms == 0:
                    metrics.tts_first_audio_ms = int((asyncio.get_event_loop().time() - llm_start) * 1000)
                if pcm:
                    await ws_send_bytes(pcm)

    # Speak remaining buffer
    if token_buffer.strip():
        async for pcm in synthesize_pcm_stream(token_buffer, lang):
            if turn_id != active_turn_id:
                return
            if pcm:
                await ws_send_bytes(pcm)

    await ws_send_json({"type": "tts_end", "turn_id": turn_id})
    
    metrics.total_turn_ms = int((asyncio.get_event_loop().time() - start_time) * 1000)
    log_turn(metrics)
    
    return full_answer
