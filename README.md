# Quantum Vidya – Unified Learning & Examination Monorepo

Quantum Vidya is a next-generation AI-powered learning platform designed to improve how students learn, practice, and understand academic concepts. It integrates an AI-powered doubt solver, a smart e-library, text-book generation, and a highly secure **AI Proctor Exam Monitor** into one unified learning ecosystem.

🔗 **GitHub Repository**: https://github.com/PKhadarkhan/122-Quantumvidya.git

---

## 🎯 Designed to Support
- Students
- Faculty
- Educational Institutions
- Hackathons & Academic Submissions

---

## 🚀 Key Capabilities

**📚 AI-Powered E-Library & Study Materials**
- Unit-wise syllabus-based content generation.
- Full textbook generation mapping to university standards.

**💬 AI Doubt Solving System (Agentic RAG)**
- Ask academic questions in natural language.
- Context-aware answers prioritizing curriculum materials.

**🔐 Secure AI Proctor Exam Monitor**
- Uses **OpenCV** to enforce webcam/audio monitoring and prevent cheating.
- Permanently assigns **Departments** to student profiles to serve hyper-targeted engineering exams.
- Fully redesigned **Premium Glassmorphic Dark Mode** aesthetic for the ultimate modern testing experience.

---

## 🏗️ System Architecture (Monorepo)
We have fully restructured the platform into a cohesive Monorepo separating Frontend assets and Backend Microservices.

### 📁 Project Structure
```text
122-Quantumvidya/
│── QuantumVidya/
│   ├── Frontend/             # All static UI assets
│   │   ├── PublicPages/      # Homepage, E-Library, AI-Solver UI
│   │   ├── ExamTemplates/    # Secure Exam Monitor HTML views
│   │   └── ExamStatic/       # Secure Exam Monitor CSS/JS
│   │
│   ├── Backend/              # Backend Services
│   │   ├── ExamService/      # Flask App, Database, OpenCV Face Tracking
│   │   ├── AIService/        # FastAPI backend, Agents, and RAG logic
│   │   └── ChatService/      # Django Assistant
│   │
│── README.md
│── index.html
```

---

## ⚙️ How to Run This Project Locally

Because this platform includes heavy backend dependencies (OpenCV, LLMs, Vector Databases), the frontend cannot be run in isolation if you want full functionality.

### 🟢 Step 1: Start the Exam Service (Main Backend)
This controls the routing, exams, and authentication.
1. Open a terminal.
2. Navigate to `QuantumVidya/Backend/ExamService/`.
3. Run `python exam_app.py`.
4. The service will start on `http://127.0.0.1:5000/`.

### 🟢 Step 2: Start the AI Service (Local LLM)
1. Open a second terminal.
2. Ensure you have Ollama running: `ollama run llama3.2`.
3. Navigate to `QuantumVidya/Backend/AIService/`.
4. Run `python -m uvicorn main:app --reload --port 8080`.

### 🟢 Step 3: Access the Platform
Simply open your web browser and navigate to:
👉 **[http://localhost:5000/](http://localhost:5000/)** (For the Exam Dashboard)
Or open `QuantumVidya/Frontend/PublicPages/index.html` to see the beautiful Landing Page which seamlessly connects to the backend!

---

## 🏁 Hackathon Submission Notes
This project aligns perfectly with the GenAIVersity Hackathon guidelines:
- **GenAI Domain**: Implements Agentic AI, LangChain, RAG, and ChromaDB.
- **Local LLM**: Fully utilizes local inference (Llama 3.2) saving API costs and demonstrating efficient prompt/context engineering.
- **Problem Domain**: Education & Secure Evaluation.
- **Deliverables**: Includes full unified UI, robust Flask & FastAPI services, required dependencies, and complete architecture documentation.
