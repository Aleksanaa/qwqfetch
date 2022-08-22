from __future__ import annotations
from os import path
from .base import config, home
from ...tools.command import RunCommand


def read_kde_qt() -> dict[str, str]:
    qt = {}
    filepaths = [f"{home}/.config/"]
    filename = "kdeglobals"
    commands = ["kf5-config", "kde4-config", "kde-config"]
    for command in commands:
        filepaths_raw = RunCommand(f"{command} --path config").read()
        if filepaths_raw:
            filepaths = filepaths_raw.strip().split(":")
        break
    filepaths.reverse()
    for filepath in filepaths:
        file = filepath + filename
        if path.exists(file):
            try:
                config.read(file)
                qt["theme"] = config["KDE"]["widgetStyle"]
                qt["icons"] = config["Icons"]["Theme"]
            except:
                pass
    return qt


qt = read_kde_qt()
