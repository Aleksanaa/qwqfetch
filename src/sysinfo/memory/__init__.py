from ... import globals

sys_name = globals.get(["platform"])[0]["name"]

if sys_name == "Linux":
    from .linux import memory_used, memory_all
else:
    pass

memory_used_mib = str(int(memory_used / (1024^2)))
memory_all_mib = str(int(memory_all / (1024^2)))

memory = "%sMiB / %sMiB" % (memory_used_mib, memory_all_mib)
