from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "CSE Chatbot"
    VERSION: str = "0.1.0"
    PORT: int = 8000
    ENVIRONMENT: str
    jwt_secret: str
    jwt_algorithm: str
    DATABASE_URL: str = "/app/db/sample_data.db"
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
    
    class Config:
        env_file = ".env"

settings = Settings()