from __future__ import annotations
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    INDEX_DIR: str = "./data/index"
    CORPUS_CSV_PATH: str = "./data/corpus.csv"
    FUZZY_THRESHOLD: int = 75
    MAX_FUZZY_CANDIDATES: int = 50
    CHUNK_SIZE: int = 100_000
    LOG_LEVEL: str = "INFO"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    WORKERS: int = 4
    ENABLE_FUZZY: bool = True
    MAX_BATCH_SIZE: int = 1000

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()