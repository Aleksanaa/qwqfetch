from __future__ import annotations
from ... import global_vars

platform_info = global_vars.get(["platform"])[0]
sys_name = platform_info["name"]


def get() -> dict[str, str]:
    # if sys_name == "Linux":
    #    from .linux import resolution
    if sys_name == "Windows":
        from .windows import resolution
    elif sys_name == "Linux":
        from .linux import resolution
    elif sys_name == "Darwin":
        from .macos import resolution
    else:
        resolution = ""

    # going to change to regex
    # def strip(name):
    #    for info in unwanted:
    #        name = name.replace(info, "")
    #    name = name.strip()
    #    return name

    return {"Resolution": resolution.strip()}
