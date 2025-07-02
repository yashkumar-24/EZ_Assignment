from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    FERNET_KEY: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    BASE_URL: str
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"

settings = Settings() 