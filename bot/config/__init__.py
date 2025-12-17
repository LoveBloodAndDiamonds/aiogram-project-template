"""Пакет с конфигурацией и логированием бота."""

__all__ = ["Configuration", "load_config", "logger", "get_logger"]

from .config import Configuration, load_config
from .logger import get_logger, logger
