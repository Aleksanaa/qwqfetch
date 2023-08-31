from ...tools import get_wmic

info = get_wmic('os get name').split('|')[0]