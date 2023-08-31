from __future__ import annotations
from . import global_vars
from .basic_system_info import *
from .default_result_list import default_result
from .tools import colors
from itertools import chain, repeat, zip_longest
from re import sub


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


def get_result(colorize: bool = True) -> str:
    colorizefunc = (
        lambda x, y, z=True: x
        if colorize == False
        else colors.colorize_str_by_ansistr(x, y, z)
    )
    # the block below system info
    color_block = colors.get_color_blocks()
    result_dict = get_result_dict()
    ascii_colors = tuple(
        # format of OS: f"{info} {sys_arch}"
        # as get_from_distro in qwqfetch is not working,
        # the `info` is the full name of the distro __in most cases__
        # so we simply get the distro name by rpartition(" ")[0]
        colors.get_ansistr_bynum(x)
        for x in colors.get_distro_colornum(result_dict["OS"].rpartition(" ")[0])
    )
    result = f"{result_dict.pop('USERNAME')}@{result_dict.pop('HOSTNAME')}"
    splitter = "-" * len(result) + "\n"
    if colorize:
        result = "@".join((colorizefunc(x, ascii_colors[0]) for x in result.split("@")))
    result += "\n" + splitter
    for key, val in result_dict.items():
        # idk why ascii_colors[1] is unused
        result += f"{colorizefunc(key, ascii_colors[0])}: {val}\n"
    return result + "\n" + color_block


def get_ascres(asc: str = "") -> str:
    """
    returns:
           |
      asc  |  result
           |
    when distro is not specified, the result would be not colored.
    """
    res = get_result()
    if asc == "":
        return res
    res = res.splitlines()

    """
    {ascline}{seperator}{sysinfo}\n
    """
    # vanilla qwqfetch prints lines without space, so here is a seperator
    seperator = "   "

    # preprocess asciiart & trim strings
    asclines = asc.splitlines()  # list of ascii_distro per line
    ascwidth = asclines[0]
    # print(repr(ascwidth), len(ascwidth))
    ascwidth = len(sub(r"\x1b\[[0-9;]+m", "", ascwidth)) * " "
    # print(repr(ascwidth), len(ascwidth))
    asclen, dictlen = len(asclines), len(res)
    if asclen < dictlen:
        asclines = chain(asclines, repeat(ascwidth, dictlen - asclen))
    result = ""
    for x, y in zip_longest(asclines, res, fillvalue=""):
        result += x + seperator + y + "\n"
    return result


def main():
    from sys import version_info, exit

    if not (version_info[0] == 3 and version_info[1] >= 7):
        exit("Sorry, Please use Python3 > 3.7")

    print(get_ascres())


if __name__ == "__main__":
    main()
