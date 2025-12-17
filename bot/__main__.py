import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from .config import get_logger, load_config
from .filters import register_filters
from .handlers import bot_commands, register_handlers
from .middlewares import register_middlewares
from .schemas import TransferData


async def start_bot():
    """Функция запускает бота."""
    try:
        # Init config
        config = load_config()

        # Init logger
        logger = get_logger(stdout_level=config.LOGGING_LEVEL)

        # Init bot
        bot = Bot(
            token=config.telegram.bot_token,
            default=DefaultBotProperties(parse_mode="HTML", link_preview_is_disabled=True),
        )

        # Dispatcher
        dp = Dispatcher(storage=MemoryStorage())

        # Handlers registration
        register_handlers(dp)

        # Middlewares registration
        register_middlewares(dp)

        # Filters registration
        register_filters(dp)

        # Register commands
        await bot.set_my_commands(commands=bot_commands)

        # Log bot startup
        logger.warning(f"Bot @{(await bot.get_me()).username} started up!")

        # Launch polling
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            skip_updates=True,
            **TransferData(
                logger=logger,
            ),  # type: ignore
        )
    except KeyboardInterrupt:
        logger.warning("Bot shutdown")
    except Exception as e:
        logger.exception(f"Error ({type(e)}) while starting bot: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
