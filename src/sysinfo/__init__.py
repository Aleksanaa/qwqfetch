from .username import username
from .hostname import hostname
from .kernel import kernel
from .os_info import osinfo
from .uptime import uptime
from .terminal import terminal
from .cpu_info import cpu_info
from .shell import shell
from .memory import memory
from .. import globals
from .board_name import board_name
from .package_count import result as package_count


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
        "Packages": package_count,
    }
    globals.set({"result": result_new})
