from os.path import expanduser
from ...tools import parse_info


def get_font() -> str:
    home_path = expanduser("~")
    try:
        konsolerc = open(f"{home_path}/.config/konsolerc").read()
        default_profile_name = parse_info.parser(konsolerc, {"DefaultProfile": "f"}, "=")["f"]
        default_profile = open(
            f"{home_path}/.local/share/konsole/{default_profile_name}"
        ).read()
        font_attr = parse_info.parser(default_profile, {"Font": "font"}, "=")["font"].split(
            ","
        )
        return f"{font_attr[0]} {font_attr[1]}"

    except (FileNotFoundError, AttributeError):
        pass
    return ""