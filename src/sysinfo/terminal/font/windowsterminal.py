from os import getenv
from pathlib import Path
from json import loads
from ....tools import get_parents


def get_font() -> str:
    font_name = "Cascadia Mono"
    font_size = "12"
    try:
        file = (
            list(
                Path(f"{getenv('LocalAppData')}\\Packages").glob(
                    "Microsoft.WindowsTerminal_*\\LocalState\\settings.json"
                )
            )[0]
            .open()
            .read()
        )
        config = loads(file)

        parents_list = get_parents()
        for current_name, next_name in zip(parents_list, parents_list[1:]):
            if next_name == "WindowsTerminal.exe":
                start_shell_name = current_name
                break

        for section in config["profiles"]["list"]:
            if "commandline" in section.keys() and section["commandline"].endswith(
                start_shell_name
            ):
                if "font" in section.keys():
                    font = section["font"]
                    if "face" in font:
                        font_name = font["face"]
                    if "size" in font:
                        font_size = font["size"]
                    break
    except:
        pass
    return f"{font_name} {font_size}"
