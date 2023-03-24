from ...tools.command import RunCommand
from ...tools.parse_info import parser

gpu_info = parser(
    RunCommand("system_profiler SPDisplaysDataType").read(),
    {"Chipset Model": "name"},
    ":",
)["name"]
