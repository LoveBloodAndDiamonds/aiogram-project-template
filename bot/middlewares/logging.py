__all__ = ["LoggingMiddleware"]

from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.config import logger
from bot.schemas import TransferData


class LoggingMiddleware(BaseMiddleware):
    """This middleware logging users activity."""

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, TransferData], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: TransferData,
    ) -> Any:
        """This method calls every update."""
        try:
            if isinstance(event, Message):
                logger.info(f"User {event.from_user.id} sent message: {event.text}")  # type: ignore
            elif isinstance(event, CallbackQuery):
                logger.info(f"User {event.from_user.id} callback query: {event.data}")
            else:
                logger.info(f"Unknown event type: {type(event)}")
        except Exception as e:
            logger.error(f"Error occurred while logging event from user ({event.__dict__}): {e}")
        return await handler(event, data)
