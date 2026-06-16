from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2", temperature=0.3, num_predict=1000)

async def generate_notes(course, topic):
    prompt = f"""
You are a brilliant academic notes generator for Quantum Vidya.
Generate highly detailed, exam-oriented notes.

Course: {course}
Topic: {topic}

Rules:
- Use perfect Markdown structure (headings, bold text, bullet points).
- Provide a clear introduction.
- Provide 5-8 detailed core concepts.
- Conclude with a real-world application or example.
- Do not add any conversational filler.
"""
    try:
        return await llm.ainvoke(prompt)
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not generate notes. Please ensure **Ollama is running** with the `llama3.2` model.\n\n```\nollama run llama3.2\n```\n\n**Error:** `{str(e)}`"

async def generate_notes_chat(message: str):
    prompt = f"""
You are a brilliant academic notes generator for Quantum Vidya.
The user is asking for notes on a specific topic.
Generate highly detailed, exam-oriented notes based on their request.

User Request: {message}

Rules:
- Focus ONLY on providing notes. Do not solve doubts unless they are part of the notes request.
- Use perfect Markdown structure (headings, bold text, bullet points).
- Provide a clear introduction.
- Provide detailed core concepts.
- Do not add any conversational filler.
"""
    try:
        return await llm.ainvoke(prompt)
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not generate notes. Please ensure **Ollama is running** with the `llama3.2` model.\n\n```\nollama run llama3.2\n```\n\n**Error:** `{str(e)}`"
