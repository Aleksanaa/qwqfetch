from ...tools import get_wmic

resolution_horizontal = get_wmic(
    "path Win32_VideoController get CurrentHorizontalResolution"
).strip()
resolution_vertical = get_wmic(
    "path Win32_VideoController get CurrentVerticalResolution"
).strip()

resolution = "{}x{}".format(resolution_horizontal, resolution_vertical)
