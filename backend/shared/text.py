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

# Markdown patterns to strip before sending text to TTS
_MARKDOWN_RE = re.compile(
    r'\*{1,3}([^*]*?)\*{1,3}'   # **bold**, *italic*, ***both***
    r'|_{1,2}([^_]*?)_{1,2}'    # __bold__, _italic_
    r'|`[^`]*?`'                # `inline code`
    r'|#{1,6}\s*'               # ## headings
    r'|\[([^\]]*?)\]\([^)]*?\)' # [link text](url) → keep link text
    r'|^\s*[-*+]\s+'            # bullet list markers at line start
    r'|^\s*\d+\.\s+',           # numbered list markers at line start
    re.MULTILINE
)

def strip_markdown(text: str) -> str:
    """Remove markdown formatting so TTS doesn't read out 'asterisk' or 'hash'."""
    # Replace markdown with just the captured text group (or empty for pure syntax)
    def _replace(m: re.Match) -> str:
        # For **bold** / *italic* / __x__ / _x_ — return the inner text
        for g in m.groups():
            if g is not None:
                return g
        return ""
    cleaned = _MARKDOWN_RE.sub(_replace, text)
    # Collapse any double spaces left behind
    cleaned = re.sub(r'  +', ' ', cleaned)
    return cleaned.strip()

def split_for_tts(text: str) -> list[str]:
    text = strip_markdown(text)  # strip before splitting so no markdown leaks to TTS
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

# Short social inputs that don't need a "let me check" filler.
# The LLM will respond instantly with an acknowledgement.
_NO_FILLER_PATTERNS = {
    "en": re.compile(
        r'^(hi|hello|hey|hii|helo|good morning|good afternoon|good evening|'
        r'ok|okay|ok ok|alright|sure|got it|i see|i understand|understood|'
        r'hmm+|hm+|uh+|um+|ah+|oh+|'
        r'yes|no|nope|yep|yeah|yup|'
        r'wait|hold on|one sec|one second|'
        r'what\??|really\??|is it\??|'
        r'nice|great|perfect|awesome|cool|good|fine|'
        r'not yet|not now|later|'
        r'can you repeat|repeat that|say again|pardon|sorry\??)$',
        re.IGNORECASE
    ),
    "hi": re.compile(
        r'^(हाँ|हां|नहीं|ठीक है|ठीक|अच्छा|समझ गया|समझ गयी|हम्म+|ओह|अरे|'
        r'हेलो|हाय|नमस्ते|सुबह|शाम|'
        r'रुकिए|एक सेकंड|वेट|'
        r'हाँ हाँ|ओके|ओक|बिल्कुल|जी|जी हाँ|जी नहीं|'
        r'क्या\??|सच में\??|अच्छा\??)$',
        re.IGNORECASE
    ),
    "gu": re.compile(
        r'^(હા|ના|ઠીક છે|ઠીક|સારું|સમજ્યો|સમજ્યા|હમ્મ+|ઓહ|અરે|'
        r'હેલો|હાય|નમસ્તે|'
        r'રાહ જુઓ|એક સેકન્ડ|'
        r'હા હા|ઓકે|બરાબર|જી|જી હા|જી ના|'
        r'શું\??|સાચે\??|અચ્છા\??)$',
        re.IGNORECASE
    ),
}

# Fillers only used for genuine questions/requests that need RAG lookup
FILLERS = {
    "en": [
        "Sure, one moment.",
        "Let me check that.",
        "On it.",
        "Give me a second.",
        "Right, let me look that up.",
    ],
    "hi": [
        "जी, एक सेकंड।",
        "हाँ, देखती हूँ।",
        "बिल्कुल, अभी बताती हूँ।",
        "जी, चेक करती हूँ।",
        "हाँ, एक पल।",
    ],
    "gu": [
        "હા, એક સેકન્ડ.",
        "જોઉં છું.",
        "ચોક્કસ, અત્યારે જ.",
        "હા, તપાસ કરું છું.",
        "એક ક્ષણ.",
    ],
}

def needs_filler(text: str, lang: str) -> bool:
    """
    Returns False for short social inputs (greetings, acks, single-word replies)
    that don't need a 'let me check' filler — the LLM responds fast enough on its own.
    Returns True for genuine questions/requests that need RAG lookup time masked.
    """
    stripped = text.strip().rstrip(".!?,")

    # Very short inputs (≤3 words) are almost always social — skip filler
    if len(stripped.split()) <= 3:
        base_lang = lang.split("-")[0].lower()
        pattern = _NO_FILLER_PATTERNS.get(base_lang, _NO_FILLER_PATTERNS["en"])
        if pattern.match(stripped):
            return False

    return True

def get_filler(lang: str) -> str:
    # Handle language codes like 'en-US' or 'hi-IN'
    base_lang = lang.split('-')[0].lower()
    options = FILLERS.get(base_lang, FILLERS["en"])
    return random.choice(options)


# ── Farewell detection ────────────────────────────────────────────────────────
# Regex-based so it catches all script variants and transliterations.
# Covers: Gujarati script, Hindi script, Latin transliterations, English.

_FAREWELL_PATTERNS = re.compile(
    # English
    r'\b(bye|goodbye|good bye|see you|see ya|take care|have a good day|have a great day|'
    r'exit|quit|end call|disconnect|'
    # English thanks
    r'thank you|thankyou|thanks|thank u|thx|'
    # Hindi transliteration
    r'alvida|khuda hafiz|shubh ratri|dhanyawad|shukriya|aabhar|'
    r'theek hai bye|bas theek hai|theek hai|aavjo|phari malishu|'
    # Gujarati transliteration
    r'aavjo|pachi malas|shu|'
    # Gujarati script
    r'આભાર|ધન્યવાદ|ધન્ય\s*વાદ|આવજો|ફરી\s*મળીશું|શુભ\s*રાત્રિ|'
    r'ઠીક\s*છે\s*બાય|બાય|ગુડ\s*બાય|'
    r'થેન્ક\s*યુ|થોન્ક\s*યુ|થેન્ક્સ|થેંક્સ|ટેન્ક્સ|'
    # Hindi script
    r'अलविदा|धन्यवाद|शुक्रिया|आभार|बाय|गुडबाय|शुभ\s*रात्रि|'
    r'ठीक\s*है\s*बाय|थैंक\s*यू|थैंक्स)',
    re.IGNORECASE
)

_THANKS_PATTERNS = re.compile(
    r'\b(thank you|thankyou|thanks|thank u|thx|'
    r'dhanyawad|shukriya|aabhar|'
    r'આભાર|ધન્યવાદ|ધન્ય\s*વાદ|થેન્ક\s*યુ|થોન્ક\s*યુ|થેન્ક્સ|થેંક્સ|ટેન્ક્સ|'
    r'धन्यवाद|शुक्रिया|आभार|थैंक\s*यू|थैंक्स)',
    re.IGNORECASE
)

def is_farewell(text: str) -> bool:
    """Returns True if the text contains a farewell or thanks expression."""
    return bool(_FAREWELL_PATTERNS.search(text))

def is_thanks(text: str) -> bool:
    """Returns True if the text contains a thanks expression."""
    return bool(_THANKS_PATTERNS.search(text))
