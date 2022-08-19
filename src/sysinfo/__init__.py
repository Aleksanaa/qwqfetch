from .. import globals
from importlib import import_module

use_threading = True

functions_list = [
    getattr(import_module(".%s" % package, __package__), "get")
    # do not use path here.
    # or zipapp and pyinstaller won't work.
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
        "system_theme",
        "terminal",
    ]
]
del import_module


def run():
    output_slot = [{}] * len(functions_list)
    if use_threading == True:
        thread_list = []

        from threading import Thread

        for index, function in enumerate(functions_list):
            thread = Thread(target=function, args=[output_slot[index]])
            thread.start()
            thread_list.append(thread)

        for thread in thread_list:
            thread.join()

    else:
        for index, function in enumerate(functions_list):
            function(output_slot[index])

    for result_dict in output_slot:
        globals.set({"result": result_dict})
