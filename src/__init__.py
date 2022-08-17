from . import globals

globals._init()

from .basic_system_info import *
from .default_result_list import default_result

globals.set(
    {
        "platform": {"name": sys_name, "type": sys_type, "arch": sys_arch},
        "result": {result: "" for result in default_result},
        "args": {},
    }
)

from . import sysinfo
sysinfo.run()


def get_result():
    result_dict = globals.get(["result"])[0]
    result = "%s@%s\n" % (result_dict.pop("USERNAME"), result_dict.pop("HOSTNAME"))
    result += "-" * (len(result) - 1) + "\n"
    for key in default_result:
        if key in result_dict.keys():
            val = result_dict[key].strip()
            if isinstance(val, str) and val != "":
                result += "%s: %s\n" % (key, val)
    return result


result = get_result()
