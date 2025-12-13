from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:1b", temperature=0.25, num_predict=500)

def generate_textbook(course, subject, chapter):
    prompt = f"""
Write structured textbook content.

Course: {course}
Subject: {subject}
Chapter: {chapter}

Include definitions and examples.
"""
    return llm.invoke(prompt)
