__all__ = ["render_start_command_template"]


START_COMMAND_TEMPLATE: str = """🤝 <b>Здравствуйте, {user_full_name}!</b>"""


def render_start_command_template(user_full_name: str) -> str:
    return START_COMMAND_TEMPLATE.format(user_full_name=user_full_name)
