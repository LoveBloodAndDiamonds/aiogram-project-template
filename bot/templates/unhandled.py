__all__ = ["render_unhandled_message_template", "render_unhandled_callback_query_template"]

UNHANDLED_MESSAGE_TEMPLATE: str = (
    "Команды не существует. Введите /help чтобы увидеть список доступных команд."
)

UNHANDLED_CALLBACK_QUERY_TEMPLATE: str = "Обработчика для этой кнопки не существует."


def render_unhandled_message_template() -> str:
    return UNHANDLED_MESSAGE_TEMPLATE


def render_unhandled_callback_query_template() -> str:
    return UNHANDLED_CALLBACK_QUERY_TEMPLATE
