from . import globals
from .basic_system_info import *
from .default_result_list import default_result

def get_result_dict():
    globals._init()

    globals.set(
        {
            "platform": {"name": sys_name, "type": sys_type, "arch": sys_arch},
            "result": {result: "" for result in default_result},
            "args": {},
        }
    )

    from . import sysinfo

    sysinfo.run()

    return globals.get(["result"])[0]


def get_result():
    result_dict = get_result_dict()
    result = "{}@{}\n".format(result_dict.pop("USERNAME"), result_dict.pop("HOSTNAME"))
    result += "-" * (len(result) - 1) + "\n"
    for key in default_result:
        if key in result_dict.keys():
            val = result_dict[key].strip()
            if isinstance(val, str) and val != "":
                result += "{}: {}\n".format(key, val)
    return result
