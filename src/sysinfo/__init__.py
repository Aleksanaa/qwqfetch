from __future__ import annotations
from os import cpu_count
from multiprocessing.pool import ThreadPool
from importlib import import_module

debug = False
threading = True

modules_name_list = [
    "board_name",
    "cpu_info",
    "desktop_environment",
    "gpu_info",
    "kernel",
    "memory",
    "os_info",
    "package_count",
    "resolution",
    "shell",
    "system_theme",
    "terminal",
    "uptime",
    "username",
]


functions_list = [
    getattr(import_module(f".{module_name}", package=__package__), "get")
    for module_name in modules_name_list
]


def run_func(func):
    if debug:
        return func()
    else:
        try:
            return func()
        except:
            return {}


def run() -> dict[str, str]:

    return_list: list[dict[str, str]] = (
        ThreadPool(cpu_count()).map(run_func, functions_list)
        if threading
        else [run_func(f) for f in functions_list]
    )
    return {k: v for d in return_list for k, v in d.items()}
