# Rule: Django Development Standards

**Trigger:** Any task involving Python, Django, or Web Development.

## Instructions

- **Architecture**: Always use the MVT (Model-View-Template) pattern. Keep business logic in `services.py` or Models, not in Views.
- **Security**: Never hardcode API keys or the `SECRET_KEY`. Use a `.env` file and `django-environ`.
- **API**: For the chat interface, prioritize **Django Channels** for WebSocket support to ensure real-time communication.
- **Environment**: Always check for a virtual environment (`venv`) before installing packages.
