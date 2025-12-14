from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .rag import solve_doubt
from .docx_agent import generate_docx
from .notes_agent import generate_notes
from .exam_agent import generate_exam
from .pyq_agent import generate_pyq
from .textbook_agent import generate_textbook

app = FastAPI(title="Offline AI E-Library Backend")

# Allow CORS for all origins (for development; restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------ DOUBT SOLVER ------------------
@app.post("/ask")
def ask(payload: dict = Body(...)):
    question = payload.get("question")
    docx = payload.get("docx", False)
    answer = solve_doubt(question)
    if docx:
        return {"answer": answer, "docx": generate_docx(answer)}
    return {"answer": answer}


# ------------------ NOTES ------------------
@app.post("/notes")
def notes(payload: dict = Body(...)):
    course = payload.get("course")
    topic = payload.get("topic")
    return {"notes": generate_notes(course, topic)}


# ------------------ EXAM (SAFE, SINGLE ENDPOINT) ------------------
@app.post("/exam")
def exam(payload: dict = Body(...)):
    course = payload.get("course")
    subject = payload.get("subject")
    level = payload.get("level")
    return generate_exam(course, subject, level)


# ------------------ PYQs ------------------
@app.post("/pyq")
def pyq(payload: dict = Body(...)):
    course = payload.get("course")
    subject = payload.get("subject")
    return {"questions": generate_pyq(course, subject)}


# ------------------ TEXTBOOK ------------------
@app.get("/textbook")
def textbook(course: str, subject: str):
    try:
        content = generate_textbook(course, subject)
        if not content:
            return {"error": "AI could not generate a textbook for this course and subject."}
        return {"textbook": content}
    except Exception as e:
        # Return the error message to the frontend for easier debugging
        return {"error": str(e)}
