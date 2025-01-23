import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import chat, health
from app.websockets import connection
import sqlite3
import os
from contextlib import asynccontextmanager

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite データベース接続
@asynccontextmanager
async def lifespan(app: FastAPI):
    db_path = settings.DATABASE_URL
    db_dir = os.path.dirname(db_path)
    print(f"os:  {os}")
    print(f"Connecting to database at {db_path}")
    print(f"os.path: {os.path}")
    print(f"Database directory: {db_dir}")
    print(f"Database exists: {os.path.exists(db_dir)}")
    # ディレクトリが存在しない場合はエラーを出力
    if not os.path.exists(db_dir):
        raise FileNotFoundError(f"Directory '{db_dir}' does not exist.")
    
    # データベース接続
    try:
        yield
    finally:
        if hasattr(app.state, 'db'):
            app.state.db.close()

app = FastAPI(lifespan=lifespan)

# ルーター
app.include_router(health.router, tags=["health"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(connection.router, prefix="/ws", tags=["websocket"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=True
    )