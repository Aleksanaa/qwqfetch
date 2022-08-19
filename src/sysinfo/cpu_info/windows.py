from ...tools import get_wmic


def convert_freq(input):
    return "%.3fGHz" % (int(input) / 1000)


cpu_info_dict = {
    "name": get_wmic("cpu get Name").strip(),
    "core": get_wmic("cpu get NumberOfCores").strip(),
    "freq": convert_freq(get_wmic("cpu get MaxClockSpeed")),
    "count": "1",
}
