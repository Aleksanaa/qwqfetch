from ...tools import get_wmic


def get_board_info():
    try:
        board_name = get_wmic('baseboard get product')
    except:
        board_name = ""

    try:
        board_vendor = get_wmic('baseboard get Manufacturer')
    except:
        board_vendor = ""

    return f"{board_vendor} {board_name}"


info = get_board_info().strip()
