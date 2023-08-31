from __future__ import annotations
from ... import global_vars


def get() -> dict[str, str]:

    sys_name = global_vars.get(["platform"])[0]["name"]

    if sys_name == "Linux":
        from .linux import memory_used, memory_all
    elif sys_name == "Windows":
        from .windows import memory_used, memory_all
    elif sys_name == "Darwin":
        from .macos import memory_used, memory_all
    else:
        return {}

    return {
        "Memory": f"{memory_used / 1024 ** 2:.2f} GiB / {memory_all / 1024 ** 2:.2f} GiB"
    }
