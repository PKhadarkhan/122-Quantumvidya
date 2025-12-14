from fastapi import FastAPI
from doubt_solver import solve_any_question

app = FastAPI(title="Standalone Offline AI Doubt Solver")

@app.post("/ai-doubt")
def ai_doubt(question: str):
    return {
        "question": question,
        "answer": solve_any_question(question)
    }
