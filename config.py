from pydantic import BaseSettings


class AppConfig(BaseSettings):
    version: str

    class Config:
        env_file = ".env"
