__all__ = ["help_command_handler"]

from aiogram import types

from bot.templates import render_help_command_template


async def help_command_handler(message: types.Message) -> types.Message:
    """Обработчик команды /help."""
    return await message.answer(render_help_command_template())
