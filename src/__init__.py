from __future__ import annotations
from . import global_vars
from .basic_system_info import *
from .default_result_list import default_result
from itertools import chain, repeat


def get_result_dict() -> dict[str, str]:
    global_vars._init()

    global_vars.set(
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
        if value
    }


def get_result(asc="") -> str:
    from . import colors
    """
    returns:
           |
      asc  |  result
           |
    when distro is not specified, the result would be not colored.
    """
    color_block = colors.get_color_blocks()
    result_dict = get_result_dict()
    # TODO: Longest Match Substring
    acd = tuple(colors.color(x) for x in colors.set_text_colors(result_dict["OS"].split(" ")[0]))  # symtoms for ascii_color_dict
    
    # preprocess asciiart & trim strings
    asclines = asc.split("\n")
    ascwidth = len(asclines[0])
    asclen, dictlen = len(asclines), len(result_dict) + 3
    if asclen < dictlen: ascs = chain(asclines, repeat(" "*ascwidth, dictlen - asclen))
    else: ascs = iter(asclines)

    # optimize io using f-string
    # TODO: optional bold text
    header = f"{acd[0]}{colors.ascii_bold}{result_dict.pop('USERNAME')}{colors.reset}@{acd[0]}{colors.ascii_bold}{result_dict.pop('HOSTNAME')}{colors.reset}\n"
    result = f"{next(ascs)}{'' if asc=='' else '   '}{header}{next(ascs)}{'' if asc=='' else '   '}{'-' * (len(header)-len(acd[0])*2-2*len(colors.reset)-2*len(colors.ascii_bold)-1)}\n"
    for key, val in result_dict.items():
        result += f"{next(ascs)}{'' if asc=='' else '   '}{acd[1]}{colors.ascii_bold}{key}:{colors.reset} {val}\n"
    result += f"{next(ascs)}{'' if asc=='' else '   '}\n"
    for color in color_block.split("\n"):  # TODO: performance optimize
        result += f"{next(ascs)}{'' if asc=='' else '   '}{color}\n"
    for i in ascs:
        result += i + "\n"  # no significance difference using str.join
    return result
