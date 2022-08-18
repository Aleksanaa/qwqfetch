from os import getlogin


def get(result):
    result["USERNAME"] = getlogin()
