import os
from .base import config, home


def read_GTK2() -> str:
    gtk2 = {}
    env = os.getenv("GTK2_RC_FILES")
    if env and len(env) != 0:
        files = env.split(":")
    else:
        files = ["%s/.gtkrc-2.0" % home]
    for file in files:
        if os.path.exists(file):
            try:
                # add a [top] to make it readable
                config.read_string("[top]\n" + open(file).read())
                gtk2["theme"] = config["top"]["gtk-theme-name"].strip('"')
                gtk2["icons"] = config["top"]["gtk-icon-theme-name"].strip('"')
                gtk2["cursor"] = config["top"]["gtk-cursor-theme-name"].strip('"')
            except:
                pass
    return gtk2

gtk2 = read_GTK2()
