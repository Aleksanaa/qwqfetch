from .username import username
from .hostname import hostname
from .kernel import kernel
from .osinfo import osinfo
from .uptime import uptime
from .. import globals


def run():
    result_new = {
        "USERNAME": username,
        "HOSTNAME": hostname,
        "Kernel": kernel,
        "OS": osinfo,
        "Uptime": uptime,
    }
    globals.set({"result": result_new})
