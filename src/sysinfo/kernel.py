from platform import release
from distro import version
from .. import globals


def get(result):
    sys_name = globals.get(["platform"])[0]["name"]
    if sys_name == "Linux":
        kernel = release()
    elif sys_name == "Darwin":
        kernel = "Darwin %s" % version()
    else:
        kernel = ""
    result["Kernel"] = kernel
