from platform import platform
from ... import globals

platform_info = globals.get(["platform"])[0]
sysname = platform_info["name"]
sysarch = platform_info["arch"]

if sysname == "Linux":
    from ..osinfo.linux import info
elif sysname == "Darwin":
    info = ""

osinfo = "%s %s" % (info, sysarch)