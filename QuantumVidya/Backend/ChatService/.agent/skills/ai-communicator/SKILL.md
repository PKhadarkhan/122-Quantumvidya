---
name: ai-communicator
description: Integrates AI agent communication into a Django project. Use this when the user wants to connect the chat UI to an LLM.
---

# AI Communicator Skill

## How to use

1. **Initialize**: Run the `setup_ai_client.py` script to generate the `ai_service.py` utility.
2. **Configure**: Prompt the agent to add `OPENAI_API_KEY` or `GEMINI_API_KEY` to the `.env` file.
3. **Integrate**: Add a post-save signal in Django to trigger AI responses when a user message is saved.

## Scripts

- `python scripts/setup_ai_client.py`: Creates the boilerplate for AI streaming.
