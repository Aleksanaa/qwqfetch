from ...tools import get_wmic


def get_cpu_info() -> dict:
    return {
        "name": get_wmic("cpu get Name").strip(),
        "core": int(get_wmic("cpu get NumberOfCores").strip()),
        "freq": int(get_wmic("cpu get MaxClockSpeed")) * 1000,
        "count": 1,
    }
