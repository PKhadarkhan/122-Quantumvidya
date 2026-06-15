from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Advanced Model with generous timeout for OpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

if os.path.exists(DB_DIR):
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
else:
    retriever = None

async def solve_doubt(question: str) -> str:
    try:
        if retriever:
            docs = retriever.invoke(question)
            context = "\n".join([doc.page_content for doc in docs])
            
            prompt = f"""
You are an advanced, highly intelligent academic professor for Quantum Vidya.
Use the following context from our E-Library to answer the student's doubt perfectly.
If the context is insufficient, rely on your advanced knowledge but prioritize the provided context.

Context:
{context}

Student's Doubt:
{question}

Provide a perfectly structured, comprehensive answer using Markdown. Include examples and clear explanations:
"""
        else:
            # No RAG database — use direct LLM knowledge
            prompt = f"""
You are an advanced, highly intelligent academic professor for Quantum Vidya.
Answer the following student's doubt clearly and comprehensively.

Student's Doubt:
{question}

Provide a perfectly structured, comprehensive answer using Markdown. Include examples and clear explanations:
"""
        
        return await llm.ainvoke(prompt)
    
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not connect to the local AI model. Please ensure **Ollama is running** with the `llama3.2` model.\n\n**How to fix:** Open a terminal and run:\n```\nollama run llama3.2\n```\n\n**Technical Error:** `{str(e)}`"
