from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "CSE Chatbot"
    VERSION: str = "0.1.0"
    PORT: int = 8000
    ENVIRONMENT: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    # DATABASE_URL: str = "/cse-project/backend/app/db/sample_data.db"
    DATABASE_URL: str = "/Users/y001850/Desktop/Temp Workspace/TENET/cse-project/backend/app/db/sample_data.db"
    NODE_ENV: str = "development"
    BACKEND_PORT: int = 8000
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # OpenAI
    OPENAI_API_KEY: str

    # Langchain
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str
    
    # Tavily
    TAVILY_API_KEY: str

    # Anthropic
    ANTHROPIC_API_KEY: str

settings = Settings()