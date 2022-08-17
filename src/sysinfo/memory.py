import psutil


def get():
    mem_all = int(psutil.virtual_memory()[0] / (1024.0**2))
    mem_used = int(psutil.virtual_memory()[3] / (1024.0**2))
    return "%sMiB / %sMiB" % (str(mem_used), str(mem_all))


memory = get()
