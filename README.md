# Quantum Vidya – Unified Learning & Examination Platform

**Quantum Vidya** is a next-generation AI-powered learning platform designed to improve how students learn, practice, and understand academic concepts. It seamlessly integrates an AI-powered doubt solver, a smart e-library, automated text-book generation, and a highly secure **AI Proctor Exam Monitor** into one unified educational ecosystem.

🔗 **GitHub Repository**: https://github.com/PKhadarkhan/122-Quantumvidya.git

---

## 🛑 Important Note on LLMs & APIs

**This project relies EXCLUSIVELY on Local LLMs (Ollama + Llama 3.2).** 
*   **NO** external Gemini APIs are used.
*   **NO** ChatGPT/OpenAI APIs are used.
*   All data, context processing, and generation occur entirely locally.

---

## 🎯 Problem Statement

Traditional educational platforms are fragmented, requiring students to use separate tools for studying, doubt-clearing, and examinations. Furthermore, remote examinations often suffer from a lack of reliable, secure, and privacy-respecting proctoring mechanisms. Institutions need a unified solution that provides intelligent academic assistance while ensuring complete academic integrity during evaluations.

## 💡 Solution Description

**Quantum Vidya** solves this fragmentation by offering a single Monorepo platform that delivers:
1. **AI-Powered E-Library & Study Materials**: Unit-wise syllabus-based content generation mapped to university standards.
2. **AI Doubt Solving System (Agentic RAG)**: Context-aware answers utilizing local vector databases and local LLMs to answer academic questions accurately.
3. **Secure AI Proctor Exam Monitor**: An advanced OpenCV-based monitoring system that tracks webcam feeds, prevents tab-switching, and enforces strict academic integrity without needing external proprietary APIs.

---

## 🚀 Key Capabilities

*   **Completely Local AI Generation**: Using Agentic RAG and Langchain with ChromaDB, powered by Llama 3.2 via Ollama. No external cloud dependencies.
*   **Intelligent Proctoring**: Enforces webcam/audio monitoring and prevents cheating through computer vision algorithms (Face detection, movement tracking).
*   **Department-Specific Testing**: Permanently assigns Departments to student profiles to serve hyper-targeted engineering exams.
*   **Modern Aesthetics**: Fully redesigned Premium Glassmorphic Dark Mode for an intuitive and distraction-free user experience.

---

## 🏗️ System Architecture (Monorepo)

The platform is structured into a cohesive Monorepo separating Frontend assets and Backend Microservices.

### 📁 Project Structure
```text
122-Quantumvidya/
│── QuantumVidya/
│   ├── Frontend/             # All static HTML/CSS/JS UI assets
│   │   ├── PublicPages/      # Homepage, E-Library, AI-Solver UI
│   │   ├── ExamTemplates/    # Secure Exam Monitor HTML views
│   │   └── ExamStatic/       # Secure Exam Monitor CSS/JS
│   │
│   ├── Backend/              # Backend Python Services
│   │   ├── ExamService/      # Flask App, Database, OpenCV Face Tracking
│   │   ├── AIService/        # FastAPI backend, Agents, and RAG logic
│   │   └── ChatService/      # Django Assistant
│   │
│── README.md                 # Unified Project Documentation
│── GUIDELINES.md
│── index.html
```

---

## ⚙️ How to Run This Project Locally

Because this platform utilizes local AI processing, please ensure your system can handle local LLM inference before starting.

### 🟢 Step 1: Start the Exam Service (Main Backend)
This controls the routing, exams, and authentication.
1. Open a terminal.
2. Navigate to `QuantumVidya/Backend/ExamService/`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python exam_app.py`.
5. The service will start on `http://127.0.0.1:5000/`.

### 🟢 Step 2: Start the AI Service (Local LLM)
1. Open a second terminal.
2. Ensure you have Ollama installed and running the local model: `ollama run llama3.2`.
3. Navigate to `QuantumVidya/Backend/AIService/`.
4. Install dependencies: `pip install -r requirements.txt`
5. Start the FastAPI server: `python -m uvicorn main:app --reload --port 8080`.

### 🟢 Step 3: Access the Platform
Simply open your web browser and navigate to:
👉 **[http://localhost:5000/](http://localhost:5000/)** (For the Exam Dashboard & Unified Platform entry)
