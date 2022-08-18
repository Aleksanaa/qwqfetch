from cmath import inf
from ... import globals

sys_name = globals.get(["platform"])[0]["name"]


def get(result):
    if sys_name == "Linux":
        from .linux import info
    elif sys_name == "Windows":
        from .windows import info
    else:
        info = ""
    result["Host"] = info
