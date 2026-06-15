from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

async def generate_pyq(course, subject):
    prompt = f"""
You are an expert exam paper setter for a university.
Generate a highly realistic "Previous Year Question Paper" (PYQ).

Course: {course}
Subject: {subject}

Rules:
- Format it beautifully in Markdown.
- Include 3 Sections: Section A (Short Answers, 5 questions), Section B (Medium Answers, 3 questions), Section C (Long/Essay Answers, 2 questions).
- Make the questions extremely relevant to standard university curriculums.
- Do not provide the answers, only the questions.
- Add marks for each question (Section A: 2 marks, Section B: 5 marks, Section C: 10 marks).
"""
    try:
        return await llm.ainvoke(prompt)
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not generate PYQs. Please ensure **Ollama is running** with the `llama3.2` model.\n\n```\nollama run llama3.2\n```\n\n**Error:** `{str(e)}`"
