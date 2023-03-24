from __future__ import annotations
from ... import global_vars

platform_info = global_vars.get(["platform"])[0]
sys_name = platform_info["name"]


def get() -> dict[str, str]:
    # if sys_name == "Linux":
    #    from .linux import gpu_info
    if sys_name == "Windows":
        from .windows import gpu_info
    elif sys_name == "Linux":
        from .linux import gpu_info
    elif sys_name == "Darwin":
        from .macos import gpu_info
    else:
        gpu_info = ""

    # going to change to regex
    # def strip(name):
    #    for info in unwanted:
    #        name = name.replace(info, "")
    #    name = name.strip()
    #    return name

    return {"GPU": gpu_info.strip()}
