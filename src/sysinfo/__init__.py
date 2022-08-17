from .username import username
from .hostname import hostname
from .kernel import kernel
from .osinfo import osinfo
from .uptime import uptime
from .terminal import terminal
from .cpuinfo import cpu_info
from .shell import shell
from .memory import memory
from .. import globals
from .boardname import board_name


def run():
    result_new = {
        "USERNAME": username,
        "HOSTNAME": hostname,
        "Kernel": kernel,
        "Host": board_name,
        "OS": osinfo,
        "Uptime": uptime,
        "Terminal": terminal,
        "CPU": cpu_info,
        "Shell": shell,
        "Memory": memory,
    }
    globals.set({"result": result_new})
