from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.chat_service import ChatService
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info("WebSocket connection established")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info("WebSocket connection closed")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        if not isinstance(message, str):
            raise TypeError("message must be a str")
        print('### send_personal_message ###', message)
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()
chat_service = ChatService(connection_manager=manager)

@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print('### data ###', data)
            logger.info(f"Received message: {data}")
            # メッセージを処理して応答を生成
            response = await chat_service.process_message(data, websocket)
            print('### response ###', response)
            # 個別のクライアントに応答を送信
            if response:  # 空の応答を送信しないようにする
                await manager.send_personal_message(response, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)