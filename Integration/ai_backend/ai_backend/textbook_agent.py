from langchain_ollama import OllamaLLM
import requests

GEMMA_API_URL = "http://localhost:11434/api/generate"  # Change this if your Gemma API runs elsewhere

llm = OllamaLLM(model="gemma3:1b", temperature=0.25, num_predict=500)

def generate_textbook(course: str, subject: str) -> str:
    prompt = f"""
You are an expert academic content creator.

Generate a FULL university-level textbook for the following:

Course: {course}
Subject: {subject}

Textbook Generation Rules:
- This must be a FULL TEXTBOOK, not notes
- Include ALL important chapters
- Each chapter must include:
  - Clear explanation
  - Definitions
  - Examples where applicable
- Use simple, student-friendly language
- Structure like a real university textbook
- No Q&A format
- No summaries only
- No bullet-only content
- Write in paragraph form with headings

Begin the textbook now.
"""
    try:
        response = requests.post(
            GEMMA_API_URL,
            json={"prompt": prompt},
            timeout=120  # Increase timeout for long generations
        )
        response.raise_for_status()
        return response.json().get("text", "")
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            f"Could not connect to Gemma 3:1b API at {GEMMA_API_URL}. "
            "Please ensure the model server is running."
        )
    except Exception as e:
        raise RuntimeError(f"Gemma 3:1b API error: {e}")
