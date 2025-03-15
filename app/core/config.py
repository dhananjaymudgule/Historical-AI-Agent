from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "Historical Monuments Bot"

    # email config
    EMAIL_SENDER: str
    EMAIL_PASSWORD: str
    SMTP_SERVER: str   
    SMTP_PORT: int  


    # API Keys
    GEMINI_API_KEY: str
    GEMINI_LLM_MODEL_NAME: str

    # params
    

    class Config:
        env_file = ".env"

settings = Settings()
