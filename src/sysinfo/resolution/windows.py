from ...tools import get_wmic

resolution_horizontal = get_wmic(
    "path Win32_VideoController get CurrentHorizontalResolution"
).strip()
resolution_vertical = get_wmic(
    "path Win32_VideoController get CurrentVerticalResolution"
).strip()

resolution = f"{resolution_horizontal}x{resolution_vertical}"
