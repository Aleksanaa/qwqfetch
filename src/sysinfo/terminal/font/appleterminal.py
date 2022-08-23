from plistlib import load, loads
from os.path import expanduser


def get_font() -> str:
    config_path = f"{expanduser('~')}/Library/Preferences/com.apple.Terminal.plist"
    with open(config_path, "rb") as config_file:
        settings: dict = load(config_file)
    default_config = settings["Startup Window Settings"]
    font_config = loads(settings["Window Settings"][default_config]["Font"])
    font_name = font_config["$objects"][2]
    font_size = int(font_config["$objects"][1]["NSSize"])
    return f"{font_name} {font_size}"
