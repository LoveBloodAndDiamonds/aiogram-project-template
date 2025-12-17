__all__ = ["start_command_handler"]

from aiogram import types

from bot.templates import render_start_command_template


async def start_command_handler(message: types.Message) -> types.Message:
    """Обработчик команды /start."""
    return await message.answer(
        render_start_command_template(user_full_name=message.from_user.full_name)  # type: ignore
    )
