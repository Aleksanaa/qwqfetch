from __future__ import annotations
from . import globals
from .basic_system_info import *
from .default_result_list import default_result


def get_result_dict() -> dict[str, str]:
    globals._init()

    globals.set(
        {
            "platform": {"name": sys_name, "type": sys_type, "arch": sys_arch},
            "result": {result: "" for result in default_result},
            "args": {},
        }
    )

    from . import sysinfo

    return {
        key: value
        for key, value in dict(
            sorted(
                sysinfo.run().items(), key=lambda pair: default_result.index(pair[0])
            )
        ).items()
        if value != ""
    }


def get_result() -> str:
    result_dict = get_result_dict()
    result = f"{result_dict.pop('USERNAME')}@{result_dict.pop('HOSTNAME')}\n"
    result += "-" * (len(result) - 1) + "\n"
    for key, val in result_dict.items():
        result += f"{key}: {val}\n"
    return result
