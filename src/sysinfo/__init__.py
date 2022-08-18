from .. import globals
from importlib import import_module
from pathlib import Path
from threading import Thread

functions_list = [
    getattr(import_module(f".{f.stem}", __package__), "get")
    for f in Path(__file__).parent.iterdir()
    if "__" not in f.stem
]
del import_module, Path


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
