from ... import globals
from .unwanted_list import unwanted

platform_info = globals.get(["platform"])[0]
sys_name = platform_info["name"]
sys_arch = platform_info["arch"]


def strip_name(name: str) -> str:
    for info in unwanted:
        name = name.replace(info, "").strip()
    # Remove existing frequency info
    if " @ " in name:
        name = name[: name.index(" @ ")]
    while "  " in name:
        name = name.replace("  ", " ")
    return name


def get() -> dict[str, str]:
    if sys_name == "Linux":
        from .linux import get_cpu_info
    elif sys_name == "Windows":
        from .windows import get_cpu_info
    else:
        get_cpu_info = lambda: {}

    info = get_cpu_info()
    output = []

    # if you can prove to me you have more than one different processors,
    # and actually using it and have python >= 3.7 installed
    # I'll change this as soon as possible.
    if "count" in info and info["count"] > 1:
        output.append(f"{info['count']}x")
    if info.get("name"):
        output.append(strip_name(info["name"]))
    if "core" in info and info["core"] > 1:
        output.append(f"({info['core']})")
    if info.get("freq"):
        output.append(f"@ {info['freq'] / 1000_000:.2f} GHz")

    return {"CPU": " ".join(output)}
