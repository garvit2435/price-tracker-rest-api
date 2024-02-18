from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    smtp_server: str
    smtp_port: int
    smtp_email: str
    smtp_password: str

    class Config:
        env_file = ".env"

settings = Settings()
