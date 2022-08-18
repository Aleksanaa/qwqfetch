from .. import globals
from importlib import import_module
from threading import Thread

functions_list = [
    getattr(import_module(".%s" % package, __package__), "get")
    for package in [
        "board_name",
        "cpu_info",
        "desktop_environment",
        "gpu_info",
        "memory",
        "os_info",
        "package_count",
        "resolution",
        "shell",
        "uptime",
        "hostname",
        "kernel",
        "username",
    ]
]
del import_module


def run():
    output_slot = [{}] * len(functions_list)
    thread_list = []

    for index, function in enumerate(functions_list):
        thread = Thread(target=function, args=[output_slot[index]])
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()
    for result_dict in output_slot:
        globals.set({"result": result_dict})
