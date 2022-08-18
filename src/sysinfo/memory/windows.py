from ...tools import get_wmic

memory_all = int(get_wmic('ComputerSystem get TotalPhysicalMemory')) / 1024
memory_free = int(get_wmic('OS get FreePhysicalMemory'))

memory_used = memory_all - memory_free