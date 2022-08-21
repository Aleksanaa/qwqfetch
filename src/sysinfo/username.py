from __future__ import annotations
from os import getlogin
from platform import node


def get() -> dict[str, str]:
    return {'USERNAME': getlogin(), 'HOSTNAME': node()}
