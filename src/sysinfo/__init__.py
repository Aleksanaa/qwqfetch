from __future__ import annotations
import os
from multiprocessing.pool import ThreadPool
from importlib import import_module

debug = False

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


def task(function):
    try:
        return function()
    except:
        return {}


def run() -> dict[str, str]:
    with ThreadPool(os.cpu_count()) as p:
        return {
            k: v
            for d in p.map(lambda f: f() if debug else task, functions_list)
            for k, v in d.items()
        }
