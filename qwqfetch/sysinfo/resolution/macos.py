from ...tools.command import RunCommand
from ...tools.parse_info import parser

resolution = parser(
    RunCommand("system_profiler SPDisplaysDataType").read(), {"Resolution": "r"}, ":"
)["r"]
horizontal = resolution.split()[0]
vertical = resolution.split()[2]
resolution = f"{horizontal}x{vertical}"
