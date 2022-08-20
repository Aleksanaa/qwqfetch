from ...globals import merge
from collections import Counter


def get_cpu_freq_sys(index):
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


def get_from_proc():
    from ...tools import parse_proc

    def strip_cpu_info(cpu_list):
        iterator = 0
        while iterator < len(cpu_list):
            iterator += 1
            del cpu_list[iterator : int(cpu_list[iterator - 1]["siblings"])]
        return cpu_list

    cpu_raw_info = strip_cpu_info(parse_proc("/proc/cpuinfo"))
    result = {
        "name": cpu_raw_info[0]["model name"],
        "core": cpu_raw_info[0]["siblings"],
        "freq": get_cpu_freq_sys(cpu_raw_info[0]["processor"]),
        "count": str(len(cpu_raw_info)),
    }
    return result


def get_from_lscpu():
    result = {}
    from os import popen

    lscpu_list = popen("lscpu").readlines()
    if lscpu_list == [""]:
        return {}

    corresponds = {
        "Socket(s):": "count",
        "CPU(s):": "core",  # is wrong but will correct later
        "CPU max MHz:": "freq",
        "CPU MHz:": "freq",
        "Model name:": "name",
    }
    for line in lscpu_list:
        for entry, key in corresponds.items():
            if line.strip().startswith(entry):
                result[key] = line.split(":", 1)[1].strip()
    try:
        result["core"] = str(int(int(result["core"]) / int(result["count"])))
        result["freq"] = "%.3fGHz" % (float(result["freq"]) / 1000)
    except (IndexError, ValueError):
        pass
    return result


for method in [get_from_proc, get_from_lscpu]:
    cpu_info_dict = {}
    merge(method(), cpu_info_dict)
    if (
        Counter(["count", "core", "freq", "name"])
        == Counter(list(cpu_info_dict.keys()))
        and "" not in cpu_info_dict.values()
    ):
        break
