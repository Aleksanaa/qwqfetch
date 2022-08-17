from distutils.log import info
from ...tools import parse_proc

info_dict = parse_proc("/proc/meminfo")[0]

memory_all = int(info_dict["MemTotal"].split()[0])
memory_available = int(info_dict["MemAvailable"].split()[0])

memory_used = memory_all - memory_available
