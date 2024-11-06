from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "CSE Chatbot"
    VERSION: str = "0.1.0"
    PORT: int = 8000    # 追加
    ENVIRONMENT: str
    jwt_secret: str
    jwt_algorithm: str
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # MongoDB
    MONGODB_URL: str 
    MONGODB_DB_NAME: str = "cse"
    
    # Redis
    REDIS_URL: str
    
    # Milvus
    MILVUS_HOST: str
    MILVUS_PORT: int
    
    # OpenAI
    OPENAI_API_KEY: str

    # Langchain
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str
    
    # Tavily
    TAVILY_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()