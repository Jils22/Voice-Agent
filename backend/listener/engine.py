import os
import asyncio
import logging
import time
from typing import Callable, Awaitable
from deepgram import AsyncDeepgramClient
from deepgram.listen.v1.types import (
    ListenV1Results,
    ListenV1UtteranceEnd,
    ListenV1SpeechStarted,
)
from settings import DEEPGRAM_API_KEY
from library.engine import retrieve

log = logging.getLogger("stt")

class DeepgramStreamingSTT:
    """
    Persistent Deepgram Live WebSocket for continuous realtime STT + Neural VAD.
    Includes Speculative Retrieval on stable interim transcripts.
    """

    def __init__(
        self,
        on_interim:        Callable[[str, str], Awaitable[None]] | None = None,
        on_final:          Callable[[str, str], Awaitable[None]] | None = None,
        on_speech_started: Callable[[], Awaitable[None]] | None = None,
        on_speculative:    Callable[[list[str]], Awaitable[None]] | None = None,
        language:          str = "multi"
    ):
        self._on_interim = on_interim
        self._on_final = on_final
        self._on_speech_started = on_speech_started
        self._on_speculative = on_speculative
        self._language = language
        
        self._socket = None
        self._ctx_mgr = None
        self._listen_task: asyncio.Task | None = None
        self._running = False
        self._lock = asyncio.Lock()

        # Speculative retrieval state
        self._last_interim = ""
        self._interim_stable_since: float = 0
        self._speculative_task: asyncio.Task | None = None

    async def start(self):
        async with self._lock:
            if self._running:
                return
            dg = AsyncDeepgramClient(api_key=DEEPGRAM_API_KEY)
            self._ctx_mgr = dg.listen.v1.connect(
                model="nova-3",
                language=self._language,
                encoding="linear16",
                sample_rate=16000,
                channels=1,
                interim_results="true",
                utterance_end_ms=1000,
                vad_events="true",
                endpointing=1000, # Set to 1000 to ensure fast response once user finishes speaking
                punctuate="true",
                smart_format="true",
            )
            self._socket = await self._ctx_mgr.__aenter__()
            self._running = True
            self._listen_task = asyncio.create_task(self._listen_loop())
            log.info("[STT] Streaming connection established.")

    async def send(self, pcm_bytes: bytes):
        if not self._running or self._socket is None:
            return
        try:
            await self._socket.send_media(pcm_bytes)
        except Exception as e:
            log.warning("[STT] send failure: %s", e)

    async def stop(self):
        async with self._lock:
            if not self._running:
                return
            self._running = False
            if self._listen_task:
                self._listen_task.cancel()
            if self._ctx_mgr is not None:
                await self._socket.send_close_stream()
                await self._ctx_mgr.__aexit__(None, None, None)
                self._ctx_mgr = None
                self._socket = None
            log.info("[STT] Streaming stopped.")

    async def _listen_loop(self):
        try:
            async for msg in self._socket:
                if not self._running: break
                if isinstance(msg, ListenV1Results):
                    await self._handle_result(msg)
                elif isinstance(msg, ListenV1SpeechStarted):
                    if self._on_speech_started:
                        await self._on_speech_started()
        except asyncio.CancelledError: pass
        except Exception as e:
            log.error("[STT] listen error: %s", e)

    async def _handle_result(self, result: ListenV1Results):
        alt = result.channel.alternatives[0]
        text = (alt.transcript or "").strip()
        if not text: return

        raw_lang = getattr(alt, "detected_language", None) or "en"
        lang = raw_lang.split("-")[0].lower()
        if lang not in {"gu", "hi", "en"}: lang = "en"

        is_final = result.is_final or result.speech_final

        if is_final:
            self._last_interim = "" # reset
            if self._on_final:
                await self._on_final(text, lang)
        else:
            # Speculative retrieval logic (Principle 6)
            now = time.perf_counter()
            if text != self._last_interim:
                self._last_interim = text
                self._interim_stable_since = now
            else:
                stable_for = now - self._interim_stable_since
                if stable_for >= 0.6 and len(text.split()) >= 4:
                    # Stable for 600ms and at least 4 words — start retrieval early
                    if self._speculative_task is None or self._speculative_task.done():
                        self._speculative_task = asyncio.create_task(
                            self._run_speculative(text)
                        )

            if self._on_interim:
                await self._on_interim(text, lang)

    async def _run_speculative(self, text: str):
        try:
            # Offload to thread to keep the STT loop fast
            chunks = await asyncio.to_thread(retrieve, text)
            if self._on_speculative:
                await self._on_speculative(chunks)
        except Exception as e:
            log.error("[STT] speculative retrieval failed: %s", e)
