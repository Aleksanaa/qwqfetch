from ... import globals

sys_name = globals.get(["platform"])[0]["name"]


def get() -> dict[str, str]:
    if sys_name == "Windows":
        de_name = "Windows Shell"
    elif sys_name == "Darwin":
        de_name = "Aqua"
    elif sys_name == "Linux":
        from os import getenv

        de_name = getenv("DESKTOP_SESSION")
        if not de_name:
            de_name = ""
    else:
        de_name = ""

    if de_name == "plasma":
        from .plasma import get as getplasma

        de_name = getplasma()
    return {"DE": de_name}
