from src.framework import *

@solution("get_board_name",1,environ.is_linux)
def get_dmi_info():
    dmi_path = "/sys/class/dmi/id/"

    try:
        board_name = open(dmi_path + "board_name").read().strip()
    except:
        board_name = ""

    try:
        board_vendor = open(dmi_path + "board_vendor").read().strip()
    except:
        board_vendor = ""

    return f"{board_vendor} {board_name}".strip()
