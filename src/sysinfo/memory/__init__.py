from ... import globals


def get(result):
    sys_name = globals.get(["platform"])[0]["name"]

    if sys_name == "Linux":
        from .linux import memory_used, memory_all
    elif sys_name == "Windows":
        from .windows import memory_used, memory_all
    else:
        pass

    memory_used_mib = int(memory_used / (1024))
    memory_all_mib = int(memory_all / (1024))

    result["Memory"] = f"{memory_used_mib}MiB / {memory_all_mib}MiB"
