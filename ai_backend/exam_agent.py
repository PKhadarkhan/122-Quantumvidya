import random

# ---------------- QUESTION BANK ----------------

QUESTION_BANK = {
    "dbms": [
        {
            "question": "What does DBMS stand for?",
            "options": {
                "a": "Data Backup Management System",
                "b": "Database Management System",
                "c": "Digital Base Modeling Software",
                "d": "Data Build Management Suite"
            },
            "correct": "b"
        },
        {
            "question": "Which key uniquely identifies a record?",
            "options": {
                "a": "Foreign Key",
                "b": "Candidate Key",
                "c": "Primary Key",
                "d": "Composite Key"
            },
            "correct": "c"
        },
        {
            "question": "Which language is used to query databases?",
            "options": {
                "a": "HTML",
                "b": "SQL",
                "c": "Java",
                "d": "Python"
            },
            "correct": "b"
        },
        {
            "question": "Which normal form removes partial dependency?",
            "options": {
                "a": "1NF",
                "b": "2NF",
                "c": "3NF",
                "d": "BCNF"
            },
            "correct": "b"
        },
        {
            "question": "Which ACID property ensures permanence?",
            "options": {
                "a": "Atomicity",
                "b": "Consistency",
                "c": "Isolation",
                "d": "Durability"
            },
            "correct": "d"
        }
    ],

    "os": [
        {
            "question": "What is a process?",
            "options": {
                "a": "Program in execution",
                "b": "Program in memory",
                "c": "Compiler",
                "d": "Thread"
            },
            "correct": "a"
        }
    ],

    "maths": [
        {
            "question": "What is the value of sin(90°)?",
            "options": {
                "a": "0",
                "b": "1",
                "c": "-1",
                "d": "Undefined"
            },
            "correct": "b"
        }
    ]
}

# ---------------- FALLBACK QUESTIONS ----------------

GENERIC_QUESTIONS = [
    {
        "question": "Which of the following best describes this subject?",
        "options": {
            "a": "Theoretical study",
            "b": "Practical application",
            "c": "Combination of theory and practice",
            "d": "Not related to academics"
        },
        "correct": "c"
    },
    {
        "question": "Which skill is most important in this subject?",
        "options": {
            "a": "Memorization",
            "b": "Problem solving",
            "c": "Guessing",
            "d": "None"
        },
        "correct": "b"
    }
]

# ---------------- EXAM GENERATOR ----------------

def generate_exam(course, subject, level):
    subject_key = subject.lower()

    questions_pool = QUESTION_BANK.get(subject_key, GENERIC_QUESTIONS)
    selected = random.sample(
        questions_pool,
        min(5, len(questions_pool))
    )

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
        "total_marks": len(exam_questions) * 4,
        "questions": exam_questions
    }
