import openai
from settings import OPENAI_API_KEY, PRIMARY_LLM_MODEL
from thinker.prompts import SYSTEM_PROMPT, format_history

client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

async def translate_query_for_retrieval(query: str, lang: str) -> str:
    """
    Translates a non-English query into English so it can match the English doc index.
    Only translates if the language is Gujarati or Hindi — English queries pass through unchanged.
    This is a lightweight single-turn call (no streaming, no history needed).
    """
    if lang == "en":
        return query

    response = await client.chat.completions.create(
        model=PRIMARY_LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a translation assistant. Translate the user's query into English. "
                    "Output ONLY the English translation — no explanation, no extra text. "
                    "Preserve technical terms like 'ledger', 'Tally', 'Suvit', 'GST' as-is."
                )
            },
            {"role": "user", "content": query}
        ],
        temperature=0.0,
        max_tokens=150,
    )
    translated = response.choices[0].message.content.strip()
    print(f"[RAG] Query translated ({lang}→en): '{query}' → '{translated}'")
    return translated

async def generate_answer_stream(query: str, retrieved_chunks: list[str], lang: str, history: list[dict]):
    """Streams tokens from GPT-4o-mini."""
    context = "\n\n".join(retrieved_chunks)
    
    # Unified Multilingual Prompt Instruction (Empowers LLM to be the master language router)
    lang_instruction = (
        "You are a multilingual voice assistant. Dynamically respond in the language spoken by the user:\n"
        "1. If the user's query is semantically or phonetically in English (even if written or transliterated in Gujarati or Devanagari scripts, e.g., 'હાઉ મેની' for 'how many', 'હાઉ કેન આઈ' for 'how can I', 'હા એમ નોટેબલ' for 'how I am not able'), respond STRICTLY in English using standard Latin characters. Use natural English conversational fillers.\n"
        "2. If the user's query is semantically or phonetically in Hindi or Hinglish, respond STRICTLY in HINDI/HINGLISH using Devanagari script. Keep common technical terms in Hinglish (e.g., 'ledger create', 'sync complete'). Use Hindi fillers like 'Ji', 'Bilkul' naturally.\n"
        "3. If the user's query is semantically and phonetically in Gujarati, respond STRICTLY in GUJARATI using Gujarati script. Keep technical terms in Hinglish naturally. Use Gujarati fillers naturally.\n"
        f"The primary target language for this call is: {lang.upper()}. Default to this target language if the query is ambiguous, but always match the user's phonetic language if they switch."
    )

    prompt = SYSTEM_PROMPT.format(
        language_instruction=lang_instruction,
        retrieved_chunks=context,
        history=format_history(history),
        query=query
    )

    response = await client.chat.completions.create(
        model=PRIMARY_LLM_MODEL,
        messages=[{"role": "system", "content": prompt}],
        stream=True,
        temperature=0.1,
    )

    async for chunk in response:
        token = chunk.choices[0].delta.content
        if token:
            yield token
