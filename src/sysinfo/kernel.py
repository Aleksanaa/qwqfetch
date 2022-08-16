from platform import release
from distro import version
from .. import globals

sysname = globals.get(["platform"])[0]['name']

if sysname == "Linux":
    kernel = release()
elif sysname == "Darwin":
    kernel = "Darwin %s" %version()
else:
    kernel = ""
