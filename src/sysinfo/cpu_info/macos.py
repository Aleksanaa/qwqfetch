from __future__ import annotations
from ...tools.command import RunCommand


def run_sysctl(key: str) -> str:
    return RunCommand(f"/usr/sbin/sysctl -n {key}").readline()


def get_cpu_info() -> dict[str, str]:
    total_cores = run_sysctl("machdep.cpu.core_count")
    per_cores = run_sysctl("machdep.cpu.cores_per_package")
    info = {
        "name": run_sysctl("machdep.cpu.brand_string"),
        "core": int(per_cores),
        "count": int(total_cores) / int(per_cores),
        "freq": int(run_sysctl("hw.cpufrequency")) / 1000,
    }
    return info
