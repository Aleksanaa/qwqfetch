from __future__ import annotations
import os
from .gtk2 import gtk2
from .gtk3 import gtk3
from .qt import qt


def read_cursor(theme_dict: dict[str, str]) -> str:
    env = os.getenv("XCURSOR_THEME")
    if env and len(env) != 0:
        return env
    for gtk in ["GTK2", "GTK3"]:
        try:
            result = theme_dict[gtk]["cursor"]
            if result:
                return result
        except KeyError:
            pass
    return ""


def read(theme_type: str, theme_dict: dict[str, str]) -> str:
    result = ""
    result_dict = {}
    for t in theme_dict.keys():
        if theme_type in theme_dict[t] and theme_dict[t][theme_type].strip() != "":
            result_dict[t] = theme_dict[t][theme_type].strip()
    # sort to prepare for pretty() and make it more pleasant
    result_dict = dict(sorted(result_dict.items()))
    while result_dict != {}:
        next_value = result_dict.get(next(iter(result_dict)))
        same_list = [i for i in result_dict if result_dict[i] == next_value]
        tag = "/".join(same_list)
        [result_dict.pop(key) for key in same_list]
        result += f"{next_value} [{tag}] "
    return pretty(result.strip())


def pretty(result: str) -> str:
    replace_dict = {"GTK2/GTK3": "GTK2/3"}
    for key, val in replace_dict.items():
        result = result.replace(key, val)
    return result.strip()


theme_dict = {"GTK2": gtk2, "GTK3": gtk3, "Qt": qt}


def get() -> dict[str, str]:
    return {
        "Theme": read("theme", theme_dict),
        "Icons": read("icons", theme_dict),
        "Cursor": read_cursor(theme_dict),
    }
