from os.path import expanduser
from ...tools import parse_info


def get_font() -> str:
    home_path = expanduser("~")
    try:
        config = open(f"{home_path}/.config/cutefishos/cutefish-terminal.conf").read()
        config: dict[str, str] = parse_info.parser(
            config, {"fontName": "font_name", "fontPointSize": "font_size"}, "="
        )
        if config["font_name"] and config["font_size"] != "":
            return f"{config['font_name']} {config['font_size']}"
    except (FileNotFoundError, AttributeError):
        pass
    return ""
