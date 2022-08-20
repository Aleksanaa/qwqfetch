from ... import globals


def get(result):
    platform_info = globals.get(["platform"])[0]
    sys_name = platform_info["name"]
    sys_arch = platform_info["arch"]

    if sys_name == "Linux":
        from .linux import info
    elif sys_name == "Darwin":
        info = ""
    elif sys_name == "Windows":
        from .windows import info
    else:
        info = ""

    result["OS"] = f"{info} {sys_arch}"
