__all__ = ["TransferData"]

from typing import TYPE_CHECKING, TypedDict

from bot.database import Database

if TYPE_CHECKING:
    from loguru import Logger


class TransferData(TypedDict):
    """
    This class contains TypedDict structure to store data which will
    transfer throw Dispatcher->Middlewares->Handlers.
    """

    db: Database
    logger: "Logger"
