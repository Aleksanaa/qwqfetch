import os
from .base import config, home


def read_GTK3() -> str:
    gtk3 = {}
    file = "%s/.config/gtk-3.0/settings.ini" % home
    if os.path.exists(file):
        try:
            config.read(file)
            gtk3["theme"] = config["Settings"]["gtk-theme-name"]
            gtk3["icons"] = config["Settings"]["gtk-icon-theme-name"]
            gtk3["cursor"] = config["Settings"]["gtk-cursor-theme-name"]
        except:
            pass
    return gtk3

gtk3 = read_GTK3()
