from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2", temperature=0.3, num_predict=1500)

async def generate_textbook(level, course, subject):
    prompt = f"""
You are an advanced textbook author and academic professor.
Write a highly structured, deeply informative textbook.

Level: {level}
Course: {course}
Subject: {subject}

Rules:
- This must be a FULL TEXTBOOK, not just notes.
- Include ALL important chapters.
- Each chapter must include clear explanations, definitions, and examples where applicable.
- Use perfect Markdown (Headings, bold text).
- Use simple, student-friendly language appropriate for the {level} level.
- Structure like a real university textbook.
- Write in paragraph form with headings, do not just give summaries or bullet points.
"""
    try:
        return await llm.ainvoke(prompt)
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not generate textbook. Please ensure **Ollama is running** with the `llama3.2` model.\n\n```\nollama run llama3.2\n```\n\n**Error:** `{str(e)}`"
