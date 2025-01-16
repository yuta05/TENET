from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Message(BaseModel):
    id: str
    content: str
    role: str
    timestamp: datetime = datetime.now()
    
class ChatResponse(BaseModel):
    message: str
    status: str
    timestamp: datetime = datetime.now()

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None