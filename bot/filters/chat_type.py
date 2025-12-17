__all__ = ["ChatTypeFilter"]

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    """Фильтр на приватные чаты."""

    def __init__(self, chat_type: str | list = "private"):
        self.chat_type = chat_type

    async def __call__(self, event: Message) -> bool:
        if isinstance(self.chat_type, list):
            return event.chat.type in self.chat_type
        return event.chat.type == self.chat_type
