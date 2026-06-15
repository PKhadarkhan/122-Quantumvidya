import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Load recent history and send it to the client
        history = await self.get_chat_history()
        for msg in history:
            await self.send(text_data=json.dumps({
                'sender': msg['sender'],
                'text': msg['text'],
                'is_ai': msg['is_ai']
            }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json.get('message', '').strip()
        
        if not message_text:
            return

        # Save user message
        await self.save_message(sender='User', text=message_text, is_ai=False)

        # Echo user message back to UI
        await self.send(text_data=json.dumps({
            'sender': 'User',
            'text': message_text,
            'is_ai': False
        }))

        # Send to agent (will be implemented in Phase 3)
        await self.process_agent_response(message_text)

    async def process_agent_response(self, user_text):
        # We will import the gemma engine here dynamically or link to it
        from agents.gemma_engine import generate_agent_response
        
        # We get the full history to send to the prompt
        history = await self.get_chat_history_for_agent()
        
        # generate_agent_response will be an async generator
        full_response = ""
        async for chunk in generate_agent_response(history):
            full_response += chunk
            # Stream chunk back to client
            await self.send(text_data=json.dumps({
                'sender': 'Gemma',
                'text': chunk,
                'is_ai': True,
                'is_stream': True
            }))

        # Once complete, save the AI's final response
        await self.save_message(sender='Gemma', text=full_response, is_ai=True)
        
        # Send a final 'done' signal
        await self.send(text_data=json.dumps({
            'sender': 'Gemma',
            'text': '',
            'is_ai': True,
            'is_stream': False,
            'done': True
        }))

    @database_sync_to_async
    def save_message(self, sender, text, is_ai):
        if text:
            Message.objects.create(sender=sender, text=text, is_ai=is_ai)

    @database_sync_to_async
    def get_chat_history(self):
        # Return last 50 messages for UI startup
        messages = Message.objects.all().order_by('timestamp')[:50]
        return [{'sender': m.sender, 'text': m.text, 'is_ai': m.is_ai} for m in messages]

    @database_sync_to_async
    def get_chat_history_for_agent(self):
        # Return all messages formatted for Gemma
        messages = Message.objects.all().order_by('timestamp')
        history_list = []
        for m in messages:
            role = 'assistant' if m.is_ai else 'user'
            history_list.append({'role': role, 'content': m.text})
        return history_list
