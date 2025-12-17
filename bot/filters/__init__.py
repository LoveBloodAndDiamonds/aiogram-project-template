"""Пакет с кастомными фильтрами для aiogram."""

__all__ = ["register_filters", "AdminFilter", "ChatTypeFilter"]

from aiogram import Dispatcher

from .admin import AdminFilter
from .chat_type import ChatTypeFilter


def register_filters(dp: Dispatcher) -> None:
    """Регистрация фильтров."""
    # Register message filters
    dp.message.filter(AdminFilter())
    dp.message.filter(ChatTypeFilter())

    # Register callback filters
    dp.callback_query.filter(AdminFilter())
    dp.callback_query.filter(ChatTypeFilter())
