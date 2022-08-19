from os import popen


def get_from_xrandr():
    try:
        xrandr = popen("xrandr --nograb --current").readlines()
        for line in xrandr:
            if "minimum" and "current" and "maximum" in line:
                resolution = line.split("current", 1)[1].split(",", 1)[0]
                return resolution.replace(" ", "")
    except (AttributeError, TypeError):
        pass
    return ""


def get_from_xwininfo():
    try:
        xwininfo = popen("xwininfo -root").readlines()
        width, height = "", ""
        for line in xwininfo:
            if "Width:" in line:
                width = line.split(":")[1].strip()
            elif "Height:" in line:
                height = line.split(":")[1].strip()
            if width != "" and height != "":
                return "{}x{}".format(width, height)
    except (AttributeError, TypeError):
        pass
    return ""


def get_from_drm():
    try:
        drm_dir = "/sys/class/drm"
        from os import scandir

        for dir in scandir(drm_dir):
            if dir.is_dir():
                resolution = open(dir.path).readline()
                return resolution
    except FileNotFoundError:
        pass
    return ""


for method in [get_from_xrandr, get_from_xwininfo, get_from_drm]:
    resolution = method()
    if resolution != "":
        break
