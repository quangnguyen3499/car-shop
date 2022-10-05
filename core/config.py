import os
import secrets
from pathlib import Path
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    API_V1_STR: str = "/api/v1"
    DATABASE_URL = os.getenv("DATABASE_URL")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

settings = Settings()