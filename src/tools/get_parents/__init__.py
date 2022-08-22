from __future__ import annotations
from os import getpid, getppid
from ... import global_vars


def get() -> list[str]:
    sys_name = global_vars.get(["platform"])[0]["name"]
    if sys_name == "Linux":
        from .linux import get_info
    elif sys_name == "Windows":
        from .windows import get_info
    try:
        return global_vars.get(["parent_list"])[0]
    except:
        pass
    try:
        pid = getppid()
    except:
        pid = getpid()
    parent_list = []
    while pid != "0":
        name, parent = get_info(pid)
        if not name:
            break
        parent_list.append(name)
        pid = parent
    global_vars.set({"parent_list": parent_list})
    return parent_list
