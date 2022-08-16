import os
from .base import config, home


def read_GTK3() -> str:
    GTK3 = {}
    file = "%s/.config/gtk-3.0/settings.ini" % home
    if os.path.exists(file):
        try:
            config.read(file)
            GTK3["theme"] = config["Settings"]["gtk-theme-name"]
            GTK3["icons"] = config["Settings"]["gtk-icon-theme-name"]
            GTK3["cursor"] = config["Settings"]["gtk-cursor-theme-name"]
        except:
            pass
    return GTK3

gtk3 = read_GTK3()
