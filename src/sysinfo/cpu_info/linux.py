from __future__ import annotations

from pathlib import Path

from ...global_vars import merge


def get_cpu_freq_sys(index: int) -> int | None:
    freq_path = Path(f"/sys/devices/system/cpu/cpu{index}/cpufreq/")
    try:
        freq_max = int((freq_path / "cpuinfo_max_freq").read_text())
        try:
            freq_bios_max = int((freq_path / "bios_limit").read_text())
            return min(freq_bios_max, freq_max)
        except:
            return freq_max
    except:
        return None


def get_from_proc() -> dict:
    from ...tools import parse_proc

    def strip_cpu_info(cpu_list):
        iterator = 0
        while iterator < len(cpu_list):
            iterator += 1
            del cpu_list[iterator: int(cpu_list[iterator - 1]["siblings"])]
        return cpu_list

    cpu_raw_info = strip_cpu_info(parse_proc("/proc/cpuinfo"))
    return {
        "name": cpu_raw_info[0]["model name"],
        "core": int(cpu_raw_info[0]["siblings"]),
        "freq": get_cpu_freq_sys(cpu_raw_info[0]["processor"]),
        "count": len(cpu_raw_info),
    }


def get_from_lscpu() -> dict:
    from ...tools.command import RunCommand

    mapping = {
        "Socket(s)": "count",
        "CPU(s)": "core",  # is wrong but will correct later
        "CPU MHz": "freq",
        "CPU max MHz": "freq",
        "Model name": "name",
    }

    lscpu: dict[str, str | int] = dict(ln.split(':', 1) for ln in RunCommand("lscpu").readlines() if ':' in ln)
    lscpu = {mapping[k.strip()]: v.strip() for k, v in lscpu.items() if k in mapping and v.strip()}

    if 'freq' in lscpu:
        lscpu['freq'] = int(lscpu['freq']) * 1000

    if 'core' in lscpu and 'count' in lscpu:
        lscpu['count'] = int(lscpu['count'])
        lscpu['core'] = int(lscpu['core']) // lscpu['count']

    return lscpu


def get_cpu_info() -> dict:
    cpu_info_dict = {}
    for method in [get_from_proc, get_from_lscpu]:
        cpu_info_dict.update({k: v for k, v in method().items() if v})
        if {"count", "core", "freq", "name"} == set(cpu_info_dict.keys()):
            break
    return cpu_info_dict
