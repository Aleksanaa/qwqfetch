from __future__ import annotations
from ... import global_vars

sys_name = global_vars.get(["platform"])[0]["name"]


def process_time(seconds: int) -> str:
    time_str = ""
    time_format = {"day": 86400, "hour": 3600, "min": 60}
    for time_type in time_format.keys():
        count = str(int(seconds / time_format[time_type]))
        if count == "1":
            time_str += f"{count} {time_type}, "
        elif count != "0":
            time_str += f"{count} {time_type}s, "
        seconds = seconds % time_format[time_type]
    return time_str.strip(", ")


def get() -> dict[str, str]:
    if sys_name == "Linux":
        from .posix import uptime_seconds
    elif sys_name == "Windows":
        from .windows import uptime_seconds
    elif sys_name == "Darwin":
        from .macos import uptime_seconds
    else:
        uptime_seconds = 0
    return {"Uptime": process_time(uptime_seconds)}
