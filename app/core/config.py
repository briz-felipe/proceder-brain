from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    pdf_service_url: str = "http://pdf_service:5060"
    openai_api_key: Optional[str] = None
    embedding_model: str = "all-MiniLM-L6-v2"
    chunk_size: int = 1000
    chunk_overlap: int = 100
    
    class Config:
        env_file = ".env"

settings = Settings()