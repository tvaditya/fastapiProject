import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER=os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER=os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT=os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB=os.getenv("POSTGRES_DB","db_jobboard")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    ACCESS_TOKEN_EXPIRE_MINUTES = 15
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"

settings = Settings()
