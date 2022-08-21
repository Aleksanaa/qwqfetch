from ... import globals


def get() -> dict[str, str]:

    sys_name = globals.get(["platform"])[0]["name"]

    if sys_name == "Linux":
        from .linux import memory_used, memory_all
    elif sys_name == "Windows":
        from .windows import memory_used, memory_all
    else:
        return {}

    return {
        "Memory": f"{memory_used / 1024 ** 2:.1f} GiB / {memory_all / 1024 ** 2:.1f} GiB"
    }
