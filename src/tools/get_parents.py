from os import getpid
from . import parse_proc


def get_info(id:str) -> tuple[str]:
    info_dict = parse_proc(f"/proc/{id}/status")[0]
    name = info_dict["Name"]
    parent = info_dict["PPid"]
    return name, parent


def get() -> list[str]:
    global parent_list
    try:
        if parent_list in globals:
            return parent_list
    except:
        pid = getpid()
        parent_list = []
        while pid != "0":
            name, parent = get_info(pid)
            parent_list.append(name)
            pid = parent
        return parent_list
