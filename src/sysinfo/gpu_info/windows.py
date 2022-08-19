from ...tools import get_wmic

gpu_info = get_wmic('path win32_VideoController get name')