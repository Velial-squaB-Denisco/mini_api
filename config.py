from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    APP_SCHEMA = os.environ.get("APP_SCHEMA", "mini_api")
    DB_URL_SYNC = os.environ.get("DB_URL_SYNC", "sqlite:///./tasks.db")

    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "mini_api")

    DB_URL_SYNC: str = os.environ.get("DB_URL_SYNC", "mini_api")

    DB_USER: str = os.environ.get("DB_USER", "")
    DB_PASS: str = os.environ.get("DB_PASS", "")
    DB_HOST: str = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT: str = os.environ.get("DB_PORT", "5432")
    DB_NAME: str = os.environ.get("DB_NAME", "mini_api")

config = Config()