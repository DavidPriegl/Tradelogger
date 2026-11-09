from pathlib import Path

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"


settings = Settings()  # pyright: ignore[reportCallIssue]