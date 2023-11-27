from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DB settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PSWD: str
    DB_NAME: str

    # Test Database Settings
    TEST_DB_HOST: str
    TEST_DB_PORT: str
    TEST_DB_USER: str
    TEST_DB_PSWD: str
    TEST_DB_NAME: str

    # Auth settings
    JWT_ALGORITHM: str
    SERVER_SECRET_KEY: str

    # Redis/Celery settings
    BROKER_URL: str
    REDIS_URL: str
    REDIS_PORT: str

    # Other settings
    PATH_TO_STATIC: str
    MODE: Literal["DEV", "TEST", "PROD"]
    PATH_TO_MOCK: str

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

    @property
    def test_database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.TEST_DB_USER}:"
            f"{self.TEST_DB_PSWD}@"
            f"{self.TEST_DB_HOST}:"
            f"{self.TEST_DB_PORT}/"
            f"{self.TEST_DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
