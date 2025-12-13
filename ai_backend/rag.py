from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="gemma3:1b",
    temperature=0.2,
    num_predict=250
)

def solve_doubt(question: str) -> str:
    prompt = f"""
Answer clearly and briefly in 5–8 lines.

Question:
{question}

Answer:
"""
    return llm.invoke(prompt)
