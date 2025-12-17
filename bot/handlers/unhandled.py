__all__ = ["unhandled_message_handler", "unhandled_callback_query_handler"]

from typing import Any

from aiogram import types

from bot.templates import (
    render_unhandled_callback_query_template,
    render_unhandled_message_template,
)


async def unhandled_message_handler(message: types.Message) -> Any:
    """Функция ловит все сообщения, которые не были пойманы другими обработчиками."""
    return await message.answer(render_unhandled_message_template())


async def unhandled_callback_query_handler(callback_query: types.CallbackQuery) -> Any:
    """Функция ловит все callback запросы, которые не были пойманы другими обработчиками."""
    return await callback_query.answer(render_unhandled_callback_query_template())
