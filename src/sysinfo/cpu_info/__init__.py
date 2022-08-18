from ... import globals
from .unwanted_list import unwanted

platform_info = globals.get(["platform"])[0]
sys_name = platform_info["name"]
sys_arch = platform_info["arch"]

def get(result):
    if sys_name == "Linux":
        from .linux import cpu_info_dict
    else:
        cpu_info_dict = None

    cpu_info = ""

    # going to change to regex
    def strip(name):
        for info in unwanted:
            name = name.replace(info, "")
        name = name.strip()
        return name


    if cpu_info_dict:
        for cpu in cpu_info_dict:
            if cpu["core"] != "1":
                cpu_info += "%s (%s)" % (strip(cpu["name"]), cpu["core"])
            else:
                cpu_info += strip(cpu["name"])
        if cpu["freq"] != "":
            cpu_info += " @ %s" % cpu["freq"]
        cpu_info += "\n"

    cpu_info = cpu_info.strip()
    result['CPU'] = cpu_info
