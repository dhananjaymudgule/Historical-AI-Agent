from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):

    # General settings
    VERSION: str = "1.0.0"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    PROJECT_NAME: str = "Historical Monuments Bot"
    PROJECT_DESCRIPTION: str = "Historical Monuments Bot"

    # API base url

    API_BASE_URL: str

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
