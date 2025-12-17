"""Пакет с регистрацией хендлеров бота и описанием команд."""

__all__ = ["bot_commands", "register_handlers"]

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import BotCommand

from .help import help_command_handler
from .start import start_command_handler
from .unhandled import unhandled_callback_query_handler, unhandled_message_handler

bot_commands = [
    BotCommand(command="start", description="Инструкция по работе c ботом"),
    BotCommand(command="help", description="Список доступных команд"),
]


def register_handlers(dp: Dispatcher) -> None:
    """Функция регистрирует хендлеры для команд на диспатчер."""
    dp.message.register(start_command_handler, Command("start"))
    dp.message.register(help_command_handler, Command("help"))

    # Fallback handlers for unprocessed events
    dp.message.register(unhandled_message_handler)
    dp.callback_query.register(unhandled_callback_query_handler)
