from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json
import os

from rag import solve_doubt
from docx_agent import generate_docx
from notes_agent import generate_notes, generate_notes_chat
from pyq_agent import generate_pyq
from textbook_agent import generate_textbook
from textbook_data import TEXTBOOKS
from library_agent import generate_library_explanation

app = FastAPI(
    title="Quantum Vidya AI Backend",
    description="AI-powered educational platform backend with LLM integration",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "error": True}
    )

# =================== HEALTH CHECK ===================
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "Quantum Vidya AI Backend v2.0"}

# =================== AI DOUBT SOLVER ===================
class AskRequest(BaseModel):
    question: str
    docx: bool = False

@app.post("/ask")
async def ask(req: AskRequest):
    if not req.question or not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    answer = await solve_doubt(req.question)
    if req.docx:
        return {"answer": answer, "docx": generate_docx(answer)}
    return {"answer": answer}

class ChatMessage(BaseModel):
    message: str

@app.post("/chat/doubts")
async def chat_doubts(req: ChatMessage):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    answer = await solve_doubt(req.message)
    return {"reply": answer}



# =================== AI NOTES ===================
class NotesRequest(BaseModel):
    course: str
    topic: str

@app.post("/notes")
async def notes(req: NotesRequest):
    if not req.course or not req.topic:
        raise HTTPException(status_code=400, detail="Course and topic are required.")
    return {"notes": await generate_notes(req.course, req.topic)}

@app.post("/chat/notes")
async def chat_notes(req: ChatMessage):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    return {"reply": await generate_notes_chat(req.message)}



# =================== PROCTORED EXAM ===================
class VideoFeedRequest(BaseModel):
    imgData: str
    testid: str = "default_test"
    voice_db: str = ""

@app.post("/video_feed")
async def video_feed(req: VideoFeedRequest):
    try:
        import camera_agent
        # camera_agent.get_frame expects the base64 string
        # remove 'data:image/jpeg;base64,' if present
        img_data = req.imgData
        if "," in img_data:
            img_data = img_data.split(",")[1]
            
        proctorData = camera_agent.get_frame(img_data)
        
        # log or process the data
        print(f"Proctoring Log for Test {req.testid}:")
        print(f"Mobile Phone Status: {proctorData['mob_status']}")
        print(f"Person Status: {proctorData['person_status']}")
        print(f"Head Movement Up/Down: {proctorData['user_move1']}")
        print(f"Head Movement L/R: {proctorData['user_move2']}")
        print(f"Eye Movement: {proctorData['eye_movements']}")
        
        return {"status": "success", "message": "recorded image of video"}
    except Exception as e:
        print("Video Feed Error:", e)
        return {"status": "error", "message": str(e)}

class WindowEventRequest(BaseModel):
    testid: str = "default_test"

@app.post("/window_event")
async def window_event(req: WindowEventRequest):
    print(f"Window Event Logged: User switched tabs/minimized window during test {req.testid}")
    return {"status": "success", "message": "recorded window"}

@app.get("/exam_data")
def get_exam_data():
    return {
        "subject": "Computer Networks",
        "total_marks": 20,
        "questions": [
            {
                "id": 1,
                "question": "What is the size of an IPv4 address?",
                "options": {"a": "16 bits", "b": "32 bits", "c": "64 bits", "d": "128 bits"},
                "correct": "b",
                "marks": 10
            },
            {
                "id": 2,
                "question": "Which layer of the OSI model is responsible for routing?",
                "options": {"a": "Data Link Layer", "b": "Transport Layer", "c": "Network Layer", "d": "Physical Layer"},
                "correct": "c",
                "marks": 10
            }
        ]
    }



# =================== PYQs ===================
class PyqRequest(BaseModel):
    course: str
    subject: str

@app.post("/pyq")
async def pyq(req: PyqRequest):
    if not req.course or not req.subject:
        raise HTTPException(status_code=400, detail="Course and subject are required.")
    return {"questions": await generate_pyq(req.course, req.subject)}


# =================== TEXTBOOK ===================
@app.get("/textbook")
def textbook(course: str, subject: str):
    return TEXTBOOKS.get(course, {}).get(subject, {})

class TextbookRequest(BaseModel):
    level: str
    course: str
    subject: str

@app.post("/textbook/generate")
async def generate_textbook_endpoint(req: TextbookRequest):
    if not req.course or not req.subject or not req.level:
        raise HTTPException(status_code=400, detail="Level, course, and subject are required.")
    return {"textbook": await generate_textbook(req.level, req.course, req.subject)}

# =================== LIBRARY CHAT ===================
@app.post("/chat/library")
async def chat_library(req: ChatMessage):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    return {"reply": await generate_library_explanation(req.message)}


# =================== AUTHENTICATION ===================
class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    age: int = None
    study: str = None
    role: str = None

class UserLogin(BaseModel):
    email: str
    password: str

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

@app.post("/api/signup")
def api_signup(user: UserSignup):
    if not user.email or not user.password or not user.name:
        raise HTTPException(status_code=400, detail="Name, email, and password are required.")
    users = load_users()
    if any(u.get("email") == user.email for u in users):
        raise HTTPException(status_code=400, detail="Email already registered.")
    users.append(user.model_dump())
    save_users(users)
    return {"message": "Account created successfully!", "user": {"name": user.name, "email": user.email, "role": user.role}}

@app.post("/api/login")
def api_login(user: UserLogin):
    if not user.email or not user.password:
        raise HTTPException(status_code=400, detail="Email and password are required.")
    users = load_users()
    for u in users:
        if u.get("email") == user.email and u.get("password") == user.password:
            return {"message": "Login successful", "user": {"name": u.get("name"), "email": u.get("email"), "role": u.get("role")}}
    raise HTTPException(status_code=401, detail="Invalid email or password.")


# =================== FRONTEND STATIC FILES (must be last) ===================
frontend_path = os.path.join(os.path.dirname(__file__), "..", "..", "Frontend", "PublicPages")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
