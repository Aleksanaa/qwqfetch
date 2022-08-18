from .gtk2 import gtk2
from .gtk3 import gtk3
from .qt import qt
import os

theme_dict = {"GTK2": gtk2, "GTK3": gtk3, "Qt": qt}


def read_cursor():
    env = os.getenv("XCURSOR_THEME")
    if len(env) != 0:
        return env
    for gtk in ["GTK2", "GTK3"]:
        result = theme_dict[gtk]["cursor"]
        if result != 0:
            return result
    return ""

def read(theme_type):
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
        result += "%s [%s] " %(next_value,tag)
    return pretty(result.strip())

def pretty(result):
    replace_dict = {'GTK2/GTK3':"GTK2/3"}
    for key,val in replace_dict.items():
        result = result.replace(key,val)
    return result.strip()

def get(result):
    result.update({'Theme':read('theme'),'Icons':read('icons'),'Cursor':read_cursor()})