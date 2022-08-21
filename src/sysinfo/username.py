from os import getlogin
from platform import node


def get_username() -> dict[str, str]:
    return {'USERNAME': getlogin(), 'HOSTNAME': node()}
