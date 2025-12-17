"""Пакет с middleware-слоем бота."""

__all__ = ["register_middlewares"]

from aiogram import Dispatcher

from .database import DatabaseMiddleware
from .exception import ExceptionMiddleware
from .logging import LoggingMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    """Регистрирует мидлвари."""

    # Register message middlewares
    dp.message.middleware(ExceptionMiddleware())
    dp.message.middleware(LoggingMiddleware())
    dp.message.outer_middleware(DatabaseMiddleware())

    # Register callback middlewares
    dp.callback_query.middleware(ExceptionMiddleware())
    dp.callback_query.middleware(LoggingMiddleware())
    dp.callback_query.outer_middleware(DatabaseMiddleware())
