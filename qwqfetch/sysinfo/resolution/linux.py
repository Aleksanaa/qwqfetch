from ...tools.command import RunCommand


def get_from_xrandr() -> str:
    try:
        xrandr = RunCommand("xrandr --nograb --current").readlines()
        for line in xrandr:
            if "minimum" and "current" and "maximum" in line:
                resolution = line.split("current", 1)[1].split(",", 1)[0]
                return resolution.replace(" ", "")
    except (AttributeError, TypeError):
        pass
    return ""


def get_from_xwininfo() -> str:
    from ...tools import parse_info

    try:
        xwininfo: str = RunCommand("xwininfo -root").read()
        xwininfo: dict["str", "str"] = parse_info(
            xwininfo, {"Width": "width", "Height": "height"}, ":"
        )
        if xwininfo["width"] and xwininfo["height"] != "":
            return f"{xwininfo['width']}x{xwininfo['height']}"
    except (AttributeError, TypeError):
        pass
    return ""


def get_from_drm() -> str:
    try:
        drm_dir = "/sys/class/drm"
        from os import scandir

        for dir in scandir(drm_dir):
            if dir.is_dir():
                resolution = open(f"{dir.path}/modes").readline()
                return resolution
    except FileNotFoundError:
        pass
    return ""


for method in [get_from_xrandr, get_from_xwininfo, get_from_drm]:
    resolution = method()
    if resolution:
        break
