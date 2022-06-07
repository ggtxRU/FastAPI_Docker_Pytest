"""
Конфигурационный файл.
"""
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """
    Определение env-переменных.

    ENVIRONMENT: среда разработки (dev, stage, prod)
    TESTING: тестовый режимм on/off  (0,1)
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    """
    @lru_cache: для кэширования настроек, чтобы get_settings вызывался только один раз,
    после запуска, если данные на выходе не изменились.
    """
    log.info("Loading config settings from the enviroment")
    return Settings()


