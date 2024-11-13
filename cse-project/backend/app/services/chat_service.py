from app.services.ai_service import AIService
from app.models.chat import Message
from datetime import datetime
import uuid

class ChatService:
    def __init__(self):
        self.ai_service = AIService()
        self.messages = []
        self.thread_id = str(uuid.uuid4())
        self.config = {
            "configurable": {
                "passenger_id": "3442 587242",
                "thread_id": self.thread_id,
            }
        }
        self._printed = set()

    async def process_message(self, message_content: str):
        # Initialize a new state for each session
        state = {
            "messages": [],
            "user_info": None,
        }
        message = Message(content=message_content, role="user", timestamp=datetime.now())
        state["messages"].append(message)
        response = await self.ai_service.generate_response(state, self.config, self._printed)
        # self._print_event(state)
        return response