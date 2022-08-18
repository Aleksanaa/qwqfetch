from ...tools import get_wmic

def get_board_info():
    dmi_path = "/sys/class/dmi/id/"
    board_name, board_vendor = "", ""
    try:
        board_name = get_wmic('baseboard get product')
    except:
        board_name = ""
    try:
        board_vendor = get_wmic('baseboard get Manufacturer')
    except:
        board_vendor = ""
    return "%s %s" % (board_vendor.strip(), board_name.strip())


info = get_board_info().strip()
