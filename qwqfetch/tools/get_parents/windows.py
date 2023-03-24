from __future__ import annotations
from ..parse_info import parser
from ..command import RunCommand


def get_info(id: str) -> tuple[str]:
    requirements = {"ParentProcessId": "parent", "Name": "name"}
    outputs: str = RunCommand(
        f"powershell Get-WmiObject Win32_Process -Filter ProcessId={id}"
    ).read()
    outputs: dict[str, str] = parser(outputs, requirements, ":")
    return outputs["name"], outputs["parent"]
