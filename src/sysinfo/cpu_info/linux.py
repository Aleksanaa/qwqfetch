from ...tools import parse_proc


def strip_cpu_info(cpu_list):
    iterator = 0
    while iterator < len(cpu_list):
        iterator += 1
        del cpu_list[iterator : int(cpu_list[iterator - 1]["siblings"])]
    return cpu_list


def get_cpu_freq(index):
    freq_path = "/sys/devices/system/cpu/cpu%s/cpufreq/" % index
    try:
        freq_max = int(open(freq_path + "cpuinfo_max_freq").read())
        try:
            freq_bios_max = int(open(freq_path + "bios_limit").read())
            return "%.3fGHz" % (min(freq_bios_max, freq_max) / 1000000)
        except:
            return "%.3fGHz" % (freq_max / 1000000)
    except:
        return ""


def form_output():
    cpu_raw_info = strip_cpu_info(parse_proc("/proc/cpuinfo"))
    result = {
        "name": cpu_raw_info[0]["model name"],
        "core": cpu_raw_info[0]["siblings"],
        "freq": get_cpu_freq(cpu_raw_info[0]["processor"]),
        "count": str(len(cpu_raw_info)),
    }
    return result


cpu_info_dict = form_output()
