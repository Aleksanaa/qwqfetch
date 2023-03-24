from __future__ import annotations
from platform import release, uname
from .. import global_vars


def get() -> dict[str, str]:
    sys_name = global_vars.get(["platform"])[0]["name"]
    if sys_name == "Linux":
        kernel = release()
    elif sys_name == "Darwin":
        kernel = f"Darwin {uname().release}"
    elif sys_name == "Windows":
        from ..tools import get_wmic

        kernel = f"NT {get_wmic('os get version')}"
    else:
        kernel = ""
    return {"Kernel": kernel}
