from ... import globals

platform_info = globals.get(["platform"])[0]
sys_name = platform_info["name"]


def get_res() -> dict[str, str]:
    #if sys_name == "Linux":
    #    from .linux import resolution
    if sys_name == "Windows":
        from .windows import resolution
    elif sys_name == "Linux":
        from .linux import resolution
    else:
        resolution = ""

    # going to change to regex
    #def strip(name):
    #    for info in unwanted:
    #        name = name.replace(info, "")
    #    name = name.strip()
    #    return name

    return {'Resolution': resolution.strip()}
