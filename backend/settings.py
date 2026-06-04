import os
from dotenv import load_dotenv

load_dotenv()

def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise RuntimeError(f"Required env var missing: {key}")
    return val

# --- API Keys ---
DEEPGRAM_API_KEY  = require_env("DEEPGRAM_API_KEY")
OPENAI_API_KEY    = require_env("OPENAI_API_KEY")
GOOGLE_API_KEY    = require_env("GOOGLE_API_KEY")
SARVAMAI_API_KEY  = os.getenv("SARVAMAI_API_KEY", "")  # optional — edge-tts fallback

# --- Model Config ---
PRIMARY_LLM_MODEL = "gpt-4o-mini"
FALLBACK_LLM_MODEL = "gemini-1.5-flash"

# --- Audio Config ---
INPUT_SAMPLE_RATE = 16000
OUTPUT_SAMPLE_RATE = 16000

# --- RAG Config ---
INDEX_DIR = os.path.join(os.path.dirname(__file__), "data", "store", "index")
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
