from __future__ import annotations
from os import getlogin
from platform import node


def get() -> dict[str, str]:
    try:
        username = getlogin()
    except FileNotFoundError:
        from getpass import getuser

        username = getuser()
    return {"USERNAME": username, "HOSTNAME": node()}
