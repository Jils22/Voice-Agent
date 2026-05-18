import openai
from settings import OPENAI_API_KEY, PRIMARY_LLM_MODEL
from thinker.prompts import SYSTEM_PROMPT, format_history

client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

async def generate_answer_stream(query: str, retrieved_chunks: list[str], lang: str, history: list[dict]):
    """Streams tokens from GPT-4o-mini."""
    context = "\n\n".join(retrieved_chunks)
    
    # Dynamic language mirroring instructions
    lang_lower = lang.lower().strip()
    if lang_lower.startswith("hi"):
        lang_instruction = (
            "1. Respond STRICTLY in HINDI/HINGLISH using Devanagari script.\n"
            "2. Use natural Hinglish/Hindi conversational fillers like 'Ji', 'Theek hai', 'Bilkul', or 'Dekhiye' naturally.\n"
            "3. Keep common English technical terms (like 'ledger', 'sync', 'upload', 'create ledger', 'select ledger') "
            "as technical Hinglish terms. You can write them in Latin letters or native Devanagari (e.g., 'ledger select कीजिये' or 'select ledger कीजिये') naturally."
        )
    elif lang_lower.startswith("gu"):
        lang_instruction = (
            "1. Respond STRICTLY in GUJARATI using Gujarati script.\n"
            "2. Use natural Gujarati conversational fillers naturally.\n"
            "3. Incorporate common English technical terms (like 'ledger', 'sync', 'upload') naturally in Gujarati."
        )
    else:
        # Default to English
        lang_instruction = (
            "1. Respond STRICTLY in English. Do not use Hindi words, phrases, or Devanagari script.\n"
            "2. Use English conversational fillers (like 'Sure', 'Okay', 'Right', 'Let me check') naturally."
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
