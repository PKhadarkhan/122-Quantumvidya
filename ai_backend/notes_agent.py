from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:1b", temperature=0.2, num_predict=200)

def generate_notes(course, topic):
    prompt = f"""
Generate exam-oriented notes.

Course: {course}
Topic: {topic}

Rules:
- Bullet points
- Simple language
- Max 8 points
"""
    return llm.invoke(prompt)
