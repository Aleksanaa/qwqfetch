import os
from .base import config, home
from ...globals import merge
from ...tools.command import RunCommand

gtk3 = {}


def read_from_config() -> None:

    file = f"{home}/.config/gtk-3.0/settings.ini"
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


def get_gsettings_function():
    de_list = ["cinnamon", "gnome", "mate"]
    failed_list = []

    def get_gsettings_on_de(key):
        for de in de_list:
            if de in failed_list:
                continue
            value = RunCommand(f"gsettings get org.{de}.desktop.interface {key}").read()
            if value != "":
                return value.strip("' \n")
            else:
                failed_list.append(de)

    return get_gsettings_on_de


def read_from_gsettings():
    get_gsettings = get_gsettings_function()
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
