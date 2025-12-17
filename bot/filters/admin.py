__all__ = ["AdminFilter"]

from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.config import load_config


class AdminFilter(BaseFilter):
    """Admin role filter"""

    _admin_id = load_config().telegram.admin_id
    """Pre-load admin id."""

    async def __call__(self, event: Message) -> bool:
        return event.chat.id == self._admin_id
