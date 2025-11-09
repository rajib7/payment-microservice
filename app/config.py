from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./payments.db"
    ENV: str = "dev"
    MOCK_GATEWAY: bool = True

settings = Settings()
