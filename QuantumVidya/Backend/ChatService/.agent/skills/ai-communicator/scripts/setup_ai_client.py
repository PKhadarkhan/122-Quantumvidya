import os

def generate_ai_service(app_name="chat"):
    content = f"""
import os
import google.generativeai as genai
from django.conf import settings

class AIService:
    def __init__(self):
        # Ensure GEMINI_API_KEY is in your .env
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_response(self, user_message, history=[]):
        \"\"\"
        Sends a message to the AI and returns the text response.
        History format: [{{'role': 'user', 'parts': ['hi']}}, ...]
        \"\"\"
        chat = self.model.start_chat(history=history)
        response = chat.send_message(user_message)
        return response.text

# Singleton instance for use across the app
ai_assistant = AIService()
"""
    
    # Create the service file in the specified app
    file_path = os.path.join(app_name, "services.py")
    with open(file_path, "w") as f:
        f.write(content.strip())
    
    print(f"Successfully created AI service at {file_path}")

if __name__ == "__main__":
    generate_ai_service()