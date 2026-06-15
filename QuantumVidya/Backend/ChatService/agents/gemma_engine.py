import json
import aiohttp

OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma3:4b"  

async def generate_agent_response(history):
    """
    history format: [{'role': 'user', 'content': 'hi'}, ...]
    This connects to Ollama's stream API using aiohttp and yields chunks of the response asynchronously.
    """
    payload = {
        "model": MODEL_NAME,
        "messages": history,
        "stream": True,
        "options": {
            "num_ctx": 8192
        }
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(OLLAMA_API_URL, json=payload) as response:
                if response.status == 200:
                    async for line in response.content:
                        if line:
                            decoded_line = line.decode('utf-8')
                            try:
                                data = json.loads(decoded_line)
                                chunk = data.get('message', {}).get('content', '')
                                if chunk:
                                    yield chunk
                                if data.get('done'):
                                    break
                            except json.JSONDecodeError:
                                pass
                else:
                    yield f"Error: Failed to connect to Ollama. HTTP Status {response.status}"
    except aiohttp.ClientError:
        yield "Error: Could not connect to Ollama. Please ensure Ollama is running (`ollama serve`)."
    except Exception as e:
        yield f"Error: An unexpected error occurred: {str(e)}"
