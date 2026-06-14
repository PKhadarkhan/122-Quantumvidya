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

## ⚙️ How to Run This Project Locally

Follow these steps to set up and run the application on your local machine.

### Prerequisites
1. **Python 3.9+** installed on your machine.
2. **Ollama** installed (from [ollama.com](https://ollama.com/)).

### Step 1: Start Ollama & Download the Model
Since this project uses Local LLMs for privacy and zero API costs, you need to pull the Llama 3.2 model:
```bash
# In your terminal, run:
ollama run llama3.2
```
*Keep Ollama running in the background.*

### Step 2: Install Backend Dependencies
Navigate to the backend directory and install the required Python packages:
```bash
cd ai_backend
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Backend
Start the backend server using Uvicorn:
```bash
python -m uvicorn main:app --reload --port 8080
```
The backend API will be available at `http://localhost:8080`. 
*Note: The FastAPI backend is configured to automatically serve the frontend files natively at the root URL.*

### Step 4: Access the Application
Open your web browser and navigate to:
```text
http://localhost:8080/
```
You are now fully ready to interact with the AI Doubt Solver, Notes Generator, Textbook Generator, PYQs, and Mock Exams!

---

## 🏁 Hackathon Submission Notes
This project aligns perfectly with the GenAIVersity Hackathon guidelines:
- **GenAI Domain**: Implements Agentic AI, LangChain, RAG, and ChromaDB.
- **Local LLM**: Fully utilizes local inference (Llama 3.2) saving API costs and demonstrating efficient prompt/context engineering.
- **Problem Domain**: Education.
- **Deliverables**: Includes full UI, robust FastAPI service, required dependencies, and complete architecture documentation.
