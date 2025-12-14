from llm_engine import llm

def solve_any_question(question: str) -> str:
    prompt = f"""
You are a universal AI doubt solver.

Answer ANY question asked by the user.
The question may be:
- Academic
- Technical
- Programming
- General knowledge
- Conceptual

Rules:
- Simple language
- Clear explanation
- Structured if needed
- 6–10 lines max

Question:
{question}

Answer:
"""
    return llm.invoke(prompt)
