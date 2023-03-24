from __future__ import annotations
from .. import parse_proc

def get_info(id: str) -> tuple[str]:
    info_dict = parse_proc(f"/proc/{id}/status")[0]
    name = info_dict["Name"]
    parent = info_dict["PPid"]
    return name, parent