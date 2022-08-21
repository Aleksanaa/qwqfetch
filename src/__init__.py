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

    return sysinfo.run()


def get_result():
    result_dict = get_result_dict()
    result = f"{result_dict.pop('USERNAME')}@{result_dict.pop('HOSTNAME')}\n"
    result += "-" * (len(result) - 1) + "\n"
    for key, val in result_dict.items():
        result += f'{key}: {val}\n'
    return result
