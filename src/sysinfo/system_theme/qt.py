from os import path
from .base import config, home
from ...tools.command import run_command


def read_KDE_Qt() -> str:
    qt = {}
    filepaths = ["%s/.config/" % home]
    filename = "kdeglobals"
    commands = ["kf5-config", "kde4-config", "kde-config"]
    for command in commands:
        filepaths_raw = run_command("%s --path config" % command).read()
        if filepaths_raw !="":
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


qt = read_KDE_Qt()
