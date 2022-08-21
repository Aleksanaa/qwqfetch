from __future__ import annotations
from ... import global_vars

sys_name = global_vars.get(["platform"])[0]["name"]


def get() -> dict[str, str]:
    if sys_name == "Linux":
        from .linux import info
    elif sys_name == "Windows":
        from .windows import info
    else:
        info = ""
    return {"Host": info}
