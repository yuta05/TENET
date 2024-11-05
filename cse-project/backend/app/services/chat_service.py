from app.services.ai_service import AIService
from app.models.chat import Message
from datetime import datetime

class ChatService:
    def __init__(self):
        self.ai_service = AIService()
        self.messages = []

    async def process_message(self, message_content: str):
        message = Message(content=message_content, role="user", timestamp=datetime.now())
        self.messages.append(message)
        response = await self.ai_service.generate_response(message)
        return response