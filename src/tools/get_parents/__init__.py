from __future__ import annotations
from os import getpid
from ... import global_vars


def get() -> list[str]:
    sys_name = global_vars.get(["platform"])[0]["name"]
    if sys_name == "Linux":
        from .linux import get_info

    global parent_list
    try:
        if parent_list in globals():
            return parent_list
    except:
        pid = getpid()
        parent_list = []
        while pid != "0":
            name, parent = get_info(pid)
            parent_list.append(name)
            pid = parent
        return parent_list
