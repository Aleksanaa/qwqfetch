from ...tools import parse_proc

info_dict = parse_proc("/proc/meminfo")[0]

memory_all = int(info_dict["MemTotal"].split()[0])
memory_available = (
    int(info_dict["MemAvailable"].split()[0])
    if "MemAvailable" in info_dict
    else int(info_dict["MemFree"].split()[0])
)

# MemFree is actually better,but following neofetch
# can avoid someone complaining the value not the same.
# When MemAvailable does not exist use MemFree instead.

memory_used = memory_all - memory_available
