__all__ = ["DatabaseMiddleware"]

from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.database import Database
from bot.schemas import TransferData


class DatabaseMiddleware(BaseMiddleware):
    """This middleware throw a Database class to handler."""

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, TransferData], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: TransferData,
    ) -> Any:
        """This method calls every update."""
        async with Database.sessionmaker() as session:
            data["db"] = Database(session)
            await handler(event, data)
