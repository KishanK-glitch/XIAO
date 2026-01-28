import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Reads GROQ_API_KEY from .env automatically
    GROQ_API_KEY: str
    MODEL_NAME: str = "llama3-70b-8192" 

    class Config:
        env_file = ".env"

# Initialize settings once
settings = Settings()