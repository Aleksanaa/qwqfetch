from ... import globals
from .unwanted_list import unwanted

platform_info = globals.get(["platform"])[0]
sys_name = platform_info["name"]
sys_arch = platform_info["arch"]


def strip(name):
    for info in unwanted:
        name = name.replace(info, "").replace("  ", " ")
        name = name.strip()
    return name


def get(result):
    if sys_name == "Linux":
        from .linux import cpu_info_dict
    elif sys_name == "Windows":
        from .windows import cpu_info_dict
    else:
        cpu_info_dict = None

    cpu_info = ""

    # if you can prove to me you have more than one different processors,
    # and actually using it and have python >= 3.7 installed
    # I'll change this as soon as possible.
    if cpu_info_dict != {}:
        if cpu_info_dict["count"] != "1" or "":
            cpu_info += f"{cpu_info_dict['count']}x "
        if cpu_info_dict["core"] != "1":
            cpu_info += f"{strip(cpu_info_dict['name'])} ({cpu_info_dict['core']})"
        else:
            cpu_info += strip(cpu_info_dict["name"])
        if cpu_info_dict["freq"] != "":
            cpu_info += f" @ {cpu_info_dict['freq']}"

    cpu_info = cpu_info.strip()
    result["CPU"] = cpu_info
