from ...tools.command import RunCommand
from ...tools.parse_info import parser

memory_all = int(RunCommand("sysctl -n hw.memsize").read()) / 1024
memory_info = parser(
    RunCommand("vm_stat").read(),
    {"Pages active": "active", "Pages wired down": "wired_down"},
    ":",
)
memory_used = (
    int(memory_info["active"].rstrip(".")) + int(memory_info["wired_down"].rstrip("."))
) * 4
