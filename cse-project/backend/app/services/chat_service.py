from fastapi import WebSocket
from app.services.ai_service import AIService
from app.models.chat import Message  # ChatMessageをMessageに変更

class ChatService:
    def __init__(self):
        self.ai_service = AIService()

    async def handle_message(self, websocket: WebSocket, message: Message):  # ChatMessageをMessageに変更
        # AIサービスを使用してメッセージを処理
        response = self.ai_service.generate_response(message.content)
        await websocket.send_text(response)