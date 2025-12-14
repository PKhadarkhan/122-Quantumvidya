from langchain_ollama import OllamaLLM

# Offline, CPU-safe, fast model
llm = OllamaLLM(
    model="gemma3:1b",
    temperature=0.3,
    num_predict=500
)
