from ... import globals

sys_name = globals.get(["platform"])[0]["name"]

if sys_name == "Linux":
    from .linux import info
elif sys_name == "Darwin":
    info = ""

board_name = info
