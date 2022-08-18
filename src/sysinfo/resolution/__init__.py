from ... import globals

platform_info = globals.get(["platform"])[0]
sys_name = platform_info["name"]

def get(result):
    #if sys_name == "Linux":
    #    from .linux import resolution
    if sys_name == "Windows":
        from .windows import resolution
    else:
        resolution = ""

    # going to change to regex
    #def strip(name):
    #    for info in unwanted:
    #        name = name.replace(info, "")
    #    name = name.strip()
    #    return name

    resolution = resolution.strip()
    result['Resolution'] = resolution
