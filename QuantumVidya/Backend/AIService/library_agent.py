from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

async def generate_library_explanation(message: str) -> str:
    prompt = f"""
You are the Quantum Vidya Library Assistant.
The user is asking for topic explanations or references from the library.
Provide a clear, educational explanation of the requested topic.
If they ask for notes, give them a structured summary.

User's Request:
{message}

Rules:
- Focus solely on explaining the topic conceptually.
- Provide a structured response with Markdown (headings, bullet points).
- Be polite and academic.
"""
    try:
        return await llm.ainvoke(prompt)
    except Exception as e:
        return f"## ⚠️ AI Service Unavailable\n\nCould not connect to the local AI model. Please ensure **Ollama is running** with the `llama3.2` model.\n\n**Error:** `{str(e)}`"
