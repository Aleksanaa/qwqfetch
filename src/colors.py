"""
In fact, as hyfetch overwrite the color of logo,
we don't need to provide that color.
Maybe provide first part of set_text_colors() is enough.
"""
from .distro_colors import colors
reset = '\033[0m'
ascii_bold = '\033[1m'
def color(colornum: str) -> str:  # see neofetch color()
    if colornum == "": return ""  # fallback
    if colornum == "reset": return reset
    if colornum == "fg" or colornum == "7":
        return f"\033[37m{reset}"
    if colornum == "#": pass  # TODO
    if int(colornum) >= 0 and int(colornum) < 7:
        return f"{reset}\033[3{colornum}m"
    return f"\03338;5;{colornum}m"

def set_text_colors(distro: str) -> tuple:
    """
    WIP: see docstr at the module
    returns: (color_one, color_two)
    if distro is "", return ("", "")
    """
    if distro == "": return ("", "")  # fallback
    if distro not in colors.keys(): return colors["Stock Linux"]
    ret = colors[distro][:2] 
    if len(ret) == 1: return (ret[0], ret[0])
    return ret
