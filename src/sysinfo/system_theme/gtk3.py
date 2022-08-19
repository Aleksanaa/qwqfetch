import os
from .base import config, home
from ...globals import merge

gtk3 = {}


def read_from_config():

    file = "%s/.config/gtk-3.0/settings.ini" % home
    if os.path.exists(file):
        try:
            config.read(file)
            merge(
                {
                    "theme": config["Settings"]["gtk-theme-name"],
                    "icons": config["Settings"]["gtk-icon-theme-name"],
                    "cursor": config["Settings"]["gtk-cursor-theme-name"],
                },
                gtk3,
            )
        except:
            pass


def get_gsettings(key):
    value = os.popen("gsettings get org.gnome.desktop.interface {}".format(key)).read()
    return value.strip("' \n")


def read_from_gsettings():
    merge(
        {
            "theme": get_gsettings("gtk-theme"),
            "icons": get_gsettings("icon-theme"),
            "cursor": get_gsettings("cursor-theme"),
        },
        gtk3,
    )


for method in [read_from_config, read_from_gsettings]:
    if gtk3 != {} and "" not in gtk3.values():
        break
    method()
