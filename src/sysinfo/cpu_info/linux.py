from src.sysinfo import cpu_info
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
    result = []
    for cpu in cpu_raw_info:
        result.append(
            {
                "name": cpu["model name"],
                "core": cpu["siblings"],
                "freq": get_cpu_freq(cpu["processor"]),
            }
        )
    return result


cpu_info_list = form_output()
