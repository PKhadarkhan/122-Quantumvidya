Objective: Use the Planning Mode to architect and build a Django-based Chat Web Project that integrates Gemma 3 4B as the core reasoning engine for AI agents.

1. Project Specifications
Backend: Django 5.x with Django Channels for WebSocket-based real-time chat.

Frontend: Tailwind CSS and Alpine.js (for a lightweight, "vibe-ready" UI).

AI Model: Gemma 3 4B (hosted locally via Ollama).

Agent Logic: Implement a "Coordinator Agent" pattern where the Django app sends user messages to Gemma 3, which then decides if it needs to call local "tools" (e.g., searching the project files or checking a database).

2. Implementation Plan (to be executed by Antigravity)
Phase 1: Environment Setup
Initialize a Python virtual environment.

Install django, channels, and daphne.

Verify that Gemma 3 4B is accessible on the system.

Phase 2: Core Architecture
Create a Django project named nero_chat.

Build a chat app with a Message model (storing sender, text, timestamp, and is_ai).

Set up a WebSocket consumer in consumers.py to handle the real-time loop.

Phase 3: Gemma 3 4B Integration
Create an agents/ directory with a gemma_engine.py module.

Implement a function generate_agent_response(history) that:

Formats the chat history into a Gemma 3 friendly prompt.

Uses the 8K context window to maintain project awareness.

Streams the response back to the WebSocket.

Phase 4: UI/UX Development
Create a "Glassmorphism" chat interface.

Ensure the agent can send Artifacts (like code snippets or markdown tables) that render correctly in the chat window.

3. Deployment & Verification
The agent must use the Built-in Browser in Antigravity to verify:

The Django server starts without errors.

WebSockets connect successfully.

Gemma 3 4B responds to a test message like "Hello, who are you?".