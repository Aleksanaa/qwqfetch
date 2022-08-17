from ... import globals

sys_type = globals.get(["platform"])[0]["type"]

if sys_type == "posix":
    from .posix import uptime_seconds
elif sys_type == "nt":
    from .windows import uptime_seconds
else:
    uptime_seconds = 0


def process_time(seconds):
    time_str = ""
    time_format = {"day": 86400, "hour": 3600, "min": 60}
    for time_type in time_format.keys():
        count = str(int(seconds / time_format[time_type]))
        if count == "1":
            time_str += "%s %s, " % (count, time_type)
        elif count != "0":
            time_str += "%s %ss, " % (count, time_type)
        seconds = seconds % time_format[time_type]
    return time_str.strip(", ")


uptime = process_time(uptime_seconds)
