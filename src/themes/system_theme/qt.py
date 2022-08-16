import os
from .base import config, home


def read_KDE_Qt() -> str:
    Qt = {}
    filepaths = ["%s/.config/" % home]
    filename = "kdeglobals"
    commands = ["kf5-config", "kde4-config", "kde-config"]
    for command in commands:
        if os.system(command) == 0:
            filepaths = os.popen("%s --path config" % command).read().strip().split(":")
            break
    filepaths.reverse()
    for filepath in filepaths:
        file = filepath + filename
        if os.path.exists(file):
            try:
                config.read(file)
                Qt["theme"] = config["KDE"]["widgetStyle"]
                Qt["icons"] = config["Icons"]["Theme"]
            except:
                pass
    return Qt

qt = read_KDE_Qt()
