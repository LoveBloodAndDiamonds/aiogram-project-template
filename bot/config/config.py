"""Конфигурационные данные и настройка логирования."""

__all__ = ["load_config", "Configuration"]

from dataclasses import dataclass
from os import getenv
from typing import Literal

from sqlalchemy import URL


@dataclass(frozen=True)
class _DatabaseConfig:
    """Database connection variables."""

    name: str | None = getenv("POSTGRES_DB")
    user: str | None = getenv("POSTGRES_USER")
    passwd: str | None = getenv("POSTGRES_PASSWORD", None)
    port: int = int(getenv("POSTGRES_PORT", "5432"))
    host: str = getenv("POSTGRES_HOST", "db")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_str(self) -> str:
        """This function build a connection string."""
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass(frozen=True)
class _TelegramConfig:
    """Telegram bot configuration."""

    bot_token: str = getenv("BOT_TOKEN")  # type: ignore
    admin_id: int = int(getenv("ADMIN_ID"))  # type: ignore


@dataclass(frozen=True)
class Configuration:
    """All in one configuration's class."""

    database: _DatabaseConfig = _DatabaseConfig()
    """Database config"""

    telegram: _TelegramConfig = _TelegramConfig()
    """Telegram config"""

    LOGGING_LEVEL: Literal["ERROR", "INFO", "DEBUG", "TRACE"] = "DEBUG"
    """Logging level"""


def load_config() -> Configuration:
    """This function load configuration."""
    return Configuration()
