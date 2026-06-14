import random
import json
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2", temperature=0.5, num_predict=1200, format="json")

# ---------------- STATIC QUESTION BANK (Fast Fallback) ----------------

QUESTION_BANK = {
    "dbms": [
        {"question": "What does DBMS stand for?", "options": {"a": "Data Backup Management System", "b": "Database Management System", "c": "Digital Base Modeling Software", "d": "Data Build Management Suite"}, "correct": "b"},
        {"question": "Which key uniquely identifies a record?", "options": {"a": "Foreign Key", "b": "Candidate Key", "c": "Primary Key", "d": "Composite Key"}, "correct": "c"},
        {"question": "Which language is used to query databases?", "options": {"a": "HTML", "b": "SQL", "c": "Java", "d": "Python"}, "correct": "b"},
        {"question": "Which normal form removes partial dependency?", "options": {"a": "1NF", "b": "2NF", "c": "3NF", "d": "BCNF"}, "correct": "b"},
        {"question": "Which ACID property ensures permanence?", "options": {"a": "Atomicity", "b": "Consistency", "c": "Isolation", "d": "Durability"}, "correct": "d"}
    ],
    "os": [
        {"question": "What is a process?", "options": {"a": "Program in execution", "b": "Program in memory", "c": "Compiler", "d": "Thread"}, "correct": "a"},
        {"question": "What is deadlock?", "options": {"a": "CPU crash", "b": "Memory overflow", "c": "Two processes waiting for each other indefinitely", "d": "Network failure"}, "correct": "c"},
        {"question": "Which scheduling is non-preemptive?", "options": {"a": "Round Robin", "b": "FCFS", "c": "SRT", "d": "Priority"}, "correct": "b"}
    ],
    "maths": [
        {"question": "What is the value of sin(90°)?", "options": {"a": "0", "b": "1", "c": "-1", "d": "Undefined"}, "correct": "b"},
        {"question": "What is the derivative of x²?", "options": {"a": "x", "b": "2x", "c": "2", "d": "x²"}, "correct": "b"},
        {"question": "The value of π (pi) is approximately?", "options": {"a": "3.14", "b": "2.71", "c": "1.41", "d": "1.73"}, "correct": "a"}
    ],
    "cn": [
        {"question": "What does OSI stand for?", "options": {"a": "Open System Interconnection", "b": "Open Software Interface", "c": "Operating System Interface", "d": "None"}, "correct": "a"},
        {"question": "Which layer handles routing?", "options": {"a": "Transport", "b": "Network", "c": "Data Link", "d": "Physical"}, "correct": "b"},
        {"question": "TCP is?", "options": {"a": "Connectionless", "b": "Unreliable", "c": "Connection-oriented and reliable", "d": "Stateless"}, "correct": "c"}
    ]
}

GENERIC_QUESTIONS = [
    {"question": "Which of the following best describes this subject?", "options": {"a": "Theoretical study", "b": "Practical application", "c": "Combination of theory and practice", "d": "Not related to academics"}, "correct": "c"},
    {"question": "Which skill is most important in this subject?", "options": {"a": "Memorization", "b": "Problem solving", "c": "Guessing", "d": "None"}, "correct": "b"}
]


# ---------------- AI EXAM GENERATOR ----------------

def _parse_ai_questions(raw_text: str, count: int = 5) -> list:
    """Try to extract JSON from LLM output, return [] on failure."""
    try:
        start = raw_text.find("[")
        end = raw_text.rfind("]") + 1
        if start != -1 and end > start:
            data = json.loads(raw_text[start:end])
            questions = []
            for idx, q in enumerate(data[:count], start=1):
                questions.append({
                    "id": idx,
                    "question": q.get("question", ""),
                    "options": q.get("options", {}),
                    "correct": q.get("correct", "a"),
                    "marks": 4
                })
            return questions
    except Exception:
        pass
    return []


async def _ai_generate_questions(course: str, subject: str, level: str, count: int = 5) -> list:
    """Use LLM to generate dynamic MCQs. Returns list of question dicts."""
    prompt = f"""
Generate exactly {count} multiple choice questions for a university exam.

Course: {course}
Subject: {subject}
Level: {level}

Return ONLY a valid JSON array. Each question must follow this exact structure:
[
  {{
    "question": "Question text here?",
    "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}},
    "correct": "b"
  }}
]

Rules:
- Questions must be relevant and academically appropriate for {level} level.
- Do NOT include any text before or after the JSON array.
- The "correct" field must be exactly one of: "a", "b", "c", or "d".
"""
    raw = await llm.ainvoke(prompt)
    return _parse_ai_questions(raw, count)


async def generate_exam(course: str, subject: str, level: str):
    """Generate exam: tries AI first, falls back to static bank."""
    
    # Try AI generation first (dynamic, subject-aware)
    try:
        ai_questions = await _ai_generate_questions(course, subject, level)
        if ai_questions:
            return {
                "course": course,
                "subject": subject,
                "level": level,
                "source": "ai",
                "total_marks": len(ai_questions) * 4,
                "questions": ai_questions
            }
    except Exception:
        pass  # Fall through to static bank

    # Static bank fallback
    subject_key = subject.lower().replace(" ", "")
    questions_pool = QUESTION_BANK.get(subject_key, GENERIC_QUESTIONS)
    selected = random.sample(questions_pool, min(5, len(questions_pool)))

    exam_questions = []
    for idx, q in enumerate(selected, start=1):
        exam_questions.append({
            "id": idx,
            "question": q["question"],
            "options": q["options"],
            "correct": q["correct"],
            "marks": 4
        })

    return {
        "course": course,
        "subject": subject,
        "level": level,
        "source": "static",
        "total_marks": len(exam_questions) * 4,
        "questions": exam_questions
    }
