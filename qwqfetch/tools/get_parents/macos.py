from __future__ import annotations
from ..command import RunCommand


def get_info(id: str) -> tuple[str]:
    line = RunCommand(f"ps -o ppid,command {id}").readlines()[1].strip()
    parent = line.split()[0]
    name = line.split()[1]
    if "/" in name:
        name = name.split("/")[-1]
    return name, parent
