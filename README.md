# Quantum Vidya – AI-Powered Learning Ecosystem

Quantum Vidya is a next-generation AI-powered learning platform designed to improve how students learn, practice, and understand academic concepts. It integrates AI-powered doubt solving, a smart e-library, text-book generation, and exam generation into one unified learning ecosystem.

🔗 **GitHub Repository**: https://github.com/PKhadarkhan/122-Quantumvidya.git

---

## 🎯 Designed to Support
- Students
- Faculty
- Educational Institutions
- Hackathons & Academic Submissions

---

## ❗ Problem Statement
Most traditional learning platforms suffer from major limitations:
- Static and non-interactive learning materials
- No personalized doubt-solving mechanisms
- Low student engagement
- Limited insights into student learning progress

As a result, students focus more on memorization than understanding, and educators lack tools to track learning effectiveness.

---

## 🚀 Solution – Quantum Vidya
Quantum Vidya introduces an AI-driven learning support platform that enhances concept clarity, engagement, and accessibility using intelligent tools like RAG and Agentic workflows.

### 🧠 Key Capabilities

**📚 AI-Powered E-Library & Study Materials**
- Unit-wise syllabus-based content generation.
- Full textbook generation mapping to university standards.
- AI-generated Previous Year Question Papers (PYQs).
- Interactive, multi-level AI Mock Exams.

**💬 AI Doubt Solving System (Agentic RAG)**
- Ask academic questions in natural language.
- Context-aware answers prioritizing curriculum materials.
- Explains complex concepts step-by-step using "advanced teaching techniques".
- Beautifully formats outputs in Markdown on the frontend.

---

## 🏗️ System Architecture
Frontend (HTML/JS) ↔ REST APIs (FastAPI) ↔ AI Agents (LangChain + Ollama) ↔ Vector DB (Chroma)

### 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Marked.js (Markdown rendering)
- **Backend**: Python, FastAPI
- **Database / Vector Store**: ChromaDB
- **AI / ML**: Ollama (Llama 3.2), LangChain, HuggingFace Embeddings (all-MiniLM-L6-v2), Retrieval-Augmented Generation (RAG).

---

## 📁 Project Structure
```text
122-Quantumvidya/
│── frontend/           # Static HTML, CSS, and JS files for the UI
│── ai_backend/         # FastAPI backend, Agents, and RAG logic
│   ├── main.py         # FastAPI App and endpoints
│   ├── rag.py          # RAG-based AI Doubt Solver
│   ├── textbook_agent.py # AI Textbook Generator
│   ├── pyq_agent.py    # AI PYQ Generator
│   ├── notes_agent.py  # AI Notes Generator
│   ├── exam_agent.py   # AI Interactive Exam Generator
│   └── requirements.txt# Backend Dependencies
│── README.md
│── GUIDELINES.md
```

---

## ⚙️ How to Run This Project Locally (Easy Step-by-Step Guide)

Follow these easy steps to get the Quantum Vidya platform running on your own machine. We use a **Local LLM** to ensure complete privacy and zero API costs!

### 📌 Prerequisites
- **Python 3.9+** installed on your computer.
- **Ollama** installed (Download from [ollama.com](https://ollama.com/)).

---

### 🟢 Step 1: Start the Local LLM (Ollama)
We use the powerful `llama3.2` model locally to power all the AI features. Open a new terminal and run:
```bash
ollama run llama3.2
```
> **Important:** Keep this terminal open in the background so the AI can process requests.

---

### 🟢 Step 2: Install Project Dependencies
Open a *second* terminal, navigate to the project directory, and install the required Python packages:
```bash
cd ai_backend
pip install -r requirements.txt
```

---

### 🟢 Step 3: Run the FastAPI Server
In the same terminal (inside the `ai_backend` folder), start the backend server:
```bash
python -m uvicorn main:app --reload --port 8080
```
> You should see a message indicating the server is running on `http://127.0.0.1:8080` or `http://localhost:8080`.

---

### 🟢 Step 4: Access the Web Application
Open your web browser (Chrome, Edge, Safari) and go to:
👉 **[http://localhost:8080/](http://localhost:8080/)**

You are now ready to interact with your local, completely free AI Educational Platform!

---

## 🏁 Hackathon Submission Notes
This project aligns perfectly with the GenAIVersity Hackathon guidelines:
- **GenAI Domain**: Implements Agentic AI, LangChain, RAG, and ChromaDB.
- **Local LLM**: Fully utilizes local inference (Llama 3.2) saving API costs and demonstrating efficient prompt/context engineering.
- **Problem Domain**: Education.
- **Deliverables**: Includes full UI, robust FastAPI service, required dependencies, and complete architecture documentation.
