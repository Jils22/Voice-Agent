import httpx
import asyncio
import re
import base64
import numpy as np
import io
import wave
from settings import SARVAMAI_API_KEY, OUTPUT_SAMPLE_RATE

# ── Sarvam bulbul:v2 — locked female voices per language ────────────────────
# 'anushka' is the best female voice for all three supported languages.
# Mapping is explicit so no language ever silently falls through to a male voice.
FEMALE_VOICE_MAP: dict[str, str] = {
    "en-IN": "anushka",
    "hi-IN": "anushka",
    "gu-IN": "anushka",
}

FADE_SAMPLES = int(OUTPUT_SAMPLE_RATE * 0.025)  # 25ms smoothing

def apply_fade_in(pcm: np.ndarray) -> np.ndarray:
    """Linear fade-in on first 25ms to avoid click at chunk start."""
    fade = np.linspace(0, 1, min(FADE_SAMPLES, len(pcm)))
    pcm[:len(fade)] = (pcm[:len(fade)] * fade).astype(np.int16)
    return pcm

def apply_fade_out(pcm: np.ndarray) -> np.ndarray:
    """Linear fade-out on last 25ms to avoid click at chunk end."""
    fade = np.linspace(1, 0, min(FADE_SAMPLES, len(pcm)))
    pcm[-len(fade):] = (pcm[-len(fade):] * fade).astype(np.int16)
    return pcm

def wav_to_int16(wav_bytes: bytes) -> np.ndarray:
    with io.BytesIO(wav_bytes) as bf:
        with wave.open(bf, 'rb') as wf:
            return np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).copy()

def _normalize_brand_names(text: str) -> str:
    """
    Replace brand/product names that TTS models mispronounce.
    enable_preprocessing MUST be False — Sarvam's own preprocessor otherwise
    overrides our substitutions before speaking.

    Strategy: Embed Devanagari (Hindi) script inline for brand names.
    bulbul:v2 is trained on code-mixed Indian text, so Devanagari characters
    have a 100% unambiguous phonetic mapping — far more reliable than any
    Latin phonetic spelling which the neural model can still misinterpret.

      - 'Suvit'  → 'सुवित'    (Devanagari — reads perfectly as "Su-vit")
      - 'Vyapar' → 'व्यापार'   (Devanagari — reads perfectly as "Vyaa-paar")
    """
    text = re.sub(r'\bSuvit\b',  'सुवित',   text, flags=re.IGNORECASE)
    text = re.sub(r'\bVyapar\b', 'व्यापार', text, flags=re.IGNORECASE)
    return text

async def synthesize_pcm_stream(text: str, lang: str, check_stale = None):
    """Synthesize one phrase chunk. Apply fade in/out for smooth boundaries."""
    # Safeguard: Skip empty or non-speakable punctuation-only strings
    if not text or not re.search(r'\w', text):
        return

    # Normalize brand names before sending to TTS
    text = _normalize_brand_names(text)

    if check_stale and check_stale():
        return

    # Map any language code variant → canonical Sarvam regional code
    # Split on "-" to handle both "en" and "en-IN" inputs.
    _base = lang.lower().split("-")[0]
    lang_map = {
        "en": "en-IN",
        "hi": "hi-IN",
        "gu": "gu-IN",
    }
    target_lang = lang_map.get(_base, "en-IN")
    # Always use the explicitly-chosen female voice for this language
    speaker_voice = FEMALE_VOICE_MAP.get(target_lang, "anushka")

    # Note: Using Sarvam API for primary, would need fallback to edge-tts if missing
    async with httpx.AsyncClient(verify=False) as client:
        url = "https://api.sarvam.ai/text-to-speech"
        headers = {"api-subscription-key": SARVAMAI_API_KEY}
        payload = {
            "inputs": [text],
            "target_language_code": target_lang,
            "speaker": speaker_voice,
            "pitch": 0,
            "pace": 1.1,
            "loudness": 1.5,
            "speech_sample_rate": OUTPUT_SAMPLE_RATE,
            "enable_preprocessing": False,
            "model": "bulbul:v2"
        }
        print(f"[TTS SEND] lang={target_lang} | text={text[:80]}")
        
        retries = 3
        delay = 0.1  # start with 100ms
        for attempt in range(retries):
            try:
                if check_stale and check_stale():
                    return
                response = await client.post(url, json=payload, headers=headers, timeout=5.0)
                if check_stale and check_stale():
                    return
                if response.status_code != 200:
                    print(f"[SARVAM ERROR {response.status_code}] {response.text}")
                response.raise_for_status()
                data = response.json()
                wav_b64 = data["audios"][0]
                wav_bytes = base64.b64decode(wav_b64)
                pcm = wav_to_int16(wav_bytes)
                pcm = apply_fade_in(apply_fade_out(pcm))

                # Stream in 8KB chunks to WebSocket
                chunk_size = 8192
                pcm_bytes = pcm.tobytes()
                for i in range(0, len(pcm_bytes), chunk_size):
                    if check_stale and check_stale():
                        return
                    yield pcm_bytes[i:i + chunk_size]
                
                # Success, exit retry loop
                return
            except (httpx.ConnectError, httpx.ConnectTimeout, httpx.HTTPStatusError) as e:
                print(f"[SARVAM RETRY] Attempt {attempt+1}/{retries} failed: {e}. Retrying in {delay}s...")
                if check_stale and check_stale():
                    return
                await asyncio.sleep(delay)
                delay *= 2  # exponential backoff
            except Exception as e:
                if check_stale and check_stale():
                    return
                import traceback
                print(f"[TTS ERROR] Permanent exception during Sarvam synthesis: {repr(text)}")
                traceback.print_exc()
                return
