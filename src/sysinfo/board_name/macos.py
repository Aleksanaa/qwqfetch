from ...tools.command import RunCommand
from ...tools.parse_info import parser


model_name = parser(
    RunCommand("system_profiler SPHardwareDataType").read(),
    {"Model Identifier": "m"},
    ":",
)["m"]


info = f"Apple {model_name}"
