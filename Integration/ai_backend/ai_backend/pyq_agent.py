from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:1b", temperature=0.3, num_predict=300)

def generate_pyq(course, subject):
    prompt = f"""
Generate Previous Year Question Paper.

Course: {course}
Subject: {subject}

Rules:
- 8–10 questions
- Exam oriented
- No answers
"""
    return llm.invoke(prompt)
