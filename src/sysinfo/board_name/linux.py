def get_dmi_info():
    dmi_path = "/sys/class/dmi/id/"
    board_name, board_vendor = "", ""
    try:
        board_name = open(dmi_path + "board_name").read().strip()
    except:
        board_name = ""
    try:
        board_vendor = open(dmi_path + "board_vendor").read().strip()
    except:
        board_vendor = ""
    return "%s %s" % (board_vendor, board_name)


info = get_dmi_info().strip()
