import re
import random

# Split at natural speech pauses — ordered by strength
SPLIT_PATTERN = re.compile(
    r'(?<=[.!?।:])\s'        # sentence end or colon
    r'|(?<=,)\s'             # comma
    r'|(?<=;)\s'             # semicolon
    r'|\n'                   # newline
)

MIN_CHUNK = 12    # start speaking sooner
MAX_CHUNK = 180   # don't let chunks get too long

def split_for_tts(text: str) -> list[str]:
    parts = SPLIT_PATTERN.split(text)
    chunks, current = [], ""
    for part in parts:
        current += part
        if len(current) >= MIN_CHUNK:
            chunks.append(current.strip())
            current = ""
    if current.strip():
        chunks.append(current.strip())
    return [c for c in chunks if c]

FILLERS = {
    "en": ["Sure, one second...", "Let me check that for you.", "Actually, let me see.", "Got it, checking now."],
    "hi": ["जी, एक सेकंड रुकिए...", "मैं अभी चेक करके बताती हूँ।", "हाँ, देख लेते हैं...", "बिल्कुल, अभी बताती हूँ।"],
    "gu": ["હા, એક સેકન્ડ...", "હું હમણાં ચેક કરી લઉં છું.", "હા, જોઈ લઈએ છીએ...", "ચોક્કસ, હમણાં જણાવું છું."],
}

def get_filler(lang: str) -> str:
    # Handle language codes like 'en-US' or 'hi-IN'
    base_lang = lang.split('-')[0].lower()
    options = FILLERS.get(base_lang, FILLERS["en"])
    return random.choice(options)
