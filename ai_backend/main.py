from fastapi import FastAPI
from fastapi.responses import JSONResponse

from rag import solve_doubt
from docx_agent import generate_docx
from notes_agent import generate_notes
from exam_agent import generate_exam
from pyq_agent import generate_pyq
from textbook_data import TEXTBOOKS

app = FastAPI(title="Offline AI E-Library Backend")


# ------------------ DOUBT SOLVER ------------------
@app.post("/ask")
def ask(question: str, docx: bool = False):
    answer = solve_doubt(question)
    if docx:
        return {"answer": answer, "docx": generate_docx(answer)}
    return {"answer": answer}


# ------------------ NOTES ------------------
@app.post("/notes")
def notes(course: str, topic: str):
    return {"notes": generate_notes(course, topic)}


# ------------------ EXAM (SAFE, SINGLE ENDPOINT) ------------------
@app.post("/exam")
def exam(course: str, subject: str, level: str):
    return generate_exam(course, subject, level)


# ------------------ PYQs ------------------
@app.post("/pyq")
def pyq(course: str, subject: str):
    return {"questions": generate_pyq(course, subject)}


# ------------------ TEXTBOOK ------------------
@app.get("/textbook")
def textbook(course: str, subject: str):
    return TEXTBOOKS.get(course, {}).get(subject, {})
