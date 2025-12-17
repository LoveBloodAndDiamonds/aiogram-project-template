__all__ = ["render_help_command_template"]


HELP_COMMAND_TEMPLATE: str = """❔ <b>Список доступных команд:</b>"""


def render_help_command_template() -> str:
    return HELP_COMMAND_TEMPLATE
