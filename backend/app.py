import os
import ssl
import sys

# ULTIMATE SSL OVERRIDE (Final Boss Patch)
def apply_ultimate_ssl_patch():
    import ssl
    try:
        # Patch the default context creator itself
        orig_create_default_context = ssl.create_default_context
        def patched_create_default_context(*args, **kwargs):
            context = orig_create_default_context(*args, **kwargs)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            return context
        ssl.create_default_context = patched_create_default_context
        
        # Patch the unverified context creator too
        ssl._create_default_https_context = ssl._create_unverified_context
        
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        orig_init = urllib3.connectionpool.HTTPConnectionPool.__init__
        def new_init(self, *args, **kwargs):
            kwargs['cert_reqs'] = 'CERT_NONE'
            kwargs['assert_hostname'] = False
            return orig_init(self, *args, **kwargs)
        urllib3.connectionpool.HTTPConnectionPool.__init__ = new_init
    except: pass

apply_ultimate_ssl_patch()

os.environ["CURL_CA_BUNDLE"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["HF_HUB_DISABLE_SSL_VERIFY"] = "1"
os.environ["GIT_SSL_NO_VERIFY"] = "true"

import json
import uuid
import asyncio
from typing import Optional
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from dataclasses import dataclass, field

from settings import DEEPGRAM_API_KEY, OPENAI_API_KEY, INDEX_DIR
from listener.engine import DeepgramStreamingSTT
from orchestrator import run_pipeline
import orchestrator as pipeline # aliased for minimal logic change

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("server")

app = FastAPI(title="Suvit Voice Agent v3", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("⚡ Warmup: Pre-loading RAG retrievers and rerankers...")
    try:
        from library.engine import get_retriever, get_reranker
        # Warmup models in background thread to avoid freezing the app initialization
        await asyncio.to_thread(get_retriever)
        await asyncio.to_thread(get_reranker)
        logger.info("🎉 Warmup complete. Hybrid search engine & reranker ready!")
    except Exception as e:
        logger.error(f"❌ Warmup failed: {e}")

@dataclass
class SessionState:
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    history: list[dict] = field(default_factory=list)
    language: str = "en"
    speculative_chunks: list[str] = field(default_factory=list)

sessions: dict[str, SessionState] = {}

@app.websocket("/ws/call")
async def voice_call(ws: WebSocket):
    await ws.accept()
    logger.info("New WebSocket connection accepted")
    
    session = SessionState()
    sessions[session.session_id] = session
    
    stt_engine: Optional[DeepgramStreamingSTT] = None

    async def on_interim(text, lang):
        # DYNAMIC VOICE REPLY: Send dynamically detected language 'lang' if using dynamic mode
        # await ws.send_json({"type": "transcript_update", "text": text, "language": lang})
        await ws.send_json({"type": "transcript_update", "text": text, "language": session.language})

    async def on_final(text, lang):
        # --- LANGUAGE SELECTION MODE ---
        # OPTION A: DYNAMIC VOICE REPLY (Agent dynamically replies in the spoken language):
        # lang_to_use = lang if lang in {"hi", "gu"} else session.language
        
        # OPTION B: LOCKED MODE (Agent strictly responds in user's pre-selected tab language):
        lang_to_use = session.language
        
        # 1. Update UI
        await ws.send_json({"type": "transcript", "user": text, "language": lang_to_use})
        
        # 2. Trigger pipeline
        turn_id = str(uuid.uuid4())
        
        # Use speculative chunks if available
        chunks_to_use = session.speculative_chunks
        session.speculative_chunks = [] # clear after use
        
        # run_pipeline will handle RAG (if chunks empty), filler, LLM, and TTS
        answer = await run_pipeline(
            text=text,
            lang=lang_to_use,
            turn_id=turn_id,
            history=session.history,
            ws_send_bytes=ws.send_bytes,
            ws_send_json=ws.send_json,
            initial_chunks=chunks_to_use
        )
        
        if answer:
            session.history.append({"role": "user", "content": text})
            session.history.append({"role": "assistant", "content": answer})
            session.history = session.history[-16:] # keep last 8 turns

    async def on_speech_started():
        # BYPASSED CLOUD VAD INTERRUPTION:
        # We strictly bypass Deepgram's cloud VAD speech start triggers on the server.
        # This is because Deepgram's cloud VAD lacks context regarding the client-side
        # mute state, hardware clicks, and high noise-rejection thresholds.
        # We rely 100% on the client's high-fidelity, mute-aware VAD in audio-processor.js 
        # to send explicit 'interrupt' events when a true user barge-in is verified.
        pass

    async def on_speculative(chunks):
        session.speculative_chunks = chunks

    try:
        while True:
            message = await ws.receive()
            
            # Binary PCM from AudioWorklet
            if message.get("bytes"):
                if stt_engine:
                    await stt_engine.send(message["bytes"])
                continue
            
            # JSON Control messages
            text_payload = message.get("text")
            if not text_payload: continue
            
            data = json.loads(text_payload)
            msg_type = data.get("type")
            
            if msg_type == "call_start":
                session.language = data.get("language", "en")
                
                # --- STT ENGINE MODE ---
                # OPTION A: DYNAMIC STT DETECTION (Deepgram auto-detects any spoken language):
                # dg_lang = "multi"
                
                # OPTION B: LOCKED STT CONFIGURATION (Locks Deepgram to improve transcription accuracy):
                dg_lang = "hi" if session.language == "hi" else ("gu" if session.language == "gu" else "en")
                
                stt_engine = DeepgramStreamingSTT(
                    on_interim=on_interim,
                    on_final=on_final,
                    on_speech_started=on_speech_started,
                    on_speculative=on_speculative,
                    language=dg_lang
                )
                await stt_engine.start()
                await ws.send_json({"type": "call_accepted", "session_id": session.session_id})
                
                # TRIGGER DIRECT GREETING (Principle: Immediate Feedback)
                greeting_text = {
                    "en": "Hello! I am your Suvit AI assistant. How can I help you today?",
                    "hi": "नमस्ते! मैं आपका सुवित एआई सहायक हूँ। मैं आपकी क्या मदद कर सकता हूँ?",
                    "gu": "નમસ્તે! હું તમારો સુવિત એઆઈ સહાયક છું. હું તમને કેવી રીતે મદદ કરી શકું?"
                }.get(session.language[:2], "Hello!")
                
                async def send_greeting():
                    try:
                        logger.info(f"[GREETING] Starting synthesis for: {greeting_text}")
                        await ws.send_json({"type": "tts_start", "turn_id": "greeting"})
                        from speaker.engine import synthesize_pcm_stream
                        async for pcm in synthesize_pcm_stream(greeting_text, session.language):
                            await ws.send_bytes(pcm)
                        await ws.send_json({"type": "tts_end", "turn_id": "greeting"})
                        logger.info("[GREETING] Sent successfully.")
                    except Exception as e:
                        logger.error(f"[GREETING ERROR] {e}")

                asyncio.create_task(send_greeting())
                
                logger.info(f"Call started and direct greeting triggered for session {session.session_id}")

            elif msg_type == "interrupt":
                # Explicit interrupt from client
                pipeline.active_turn_id = None
                await ws.send_json({"type": "clear_queue"})
                logger.info(f"Interrupt received for session {session.session_id}")

            elif msg_type == "call_end":
                break

    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for session {session.session_id}")
    except Exception as e:
        logger.error(f"Error in session {session.session_id}: {e}")
    finally:
        if stt_engine:
            await stt_engine.stop()
        if session.session_id in sessions:
            del sessions[session.session_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
