from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DB settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PSWD: str
    DB_NAME: str

    # Auth settings
    JWT_ALGORITHM: str
    SERVER_SECRET_KEY: str

    # Redis/Celery settings
    BROKER_URL: str
    REDIS_URL: str
    REDIS_PORT: str

    # Other settings
    PATH_TO_STATIC: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:"
            f"{self.DB_PSWD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
