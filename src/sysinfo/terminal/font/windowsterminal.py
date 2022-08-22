from os import getenv
from pathlib import Path
from json import loads
from ....tools import get_parents


def get_font() -> str:
    font = "Cascadia Mono"
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

        for name in get_parents():
            if name != "python.exe":
                shell_name = name
                break

        for section in config["profiles"]["list"]:
            if "commandline" in section.keys() and section["commandline"].endswith(
                shell_name
            ):
                if "font" in section.keys():
                    font = section["font"]["face"]
                    break
    except:
        pass
    return font
