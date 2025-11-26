from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Intelligent Financial Dashboard"

    class Config:
        env_file = ".env"

settings = Settings()
