from os import popen


def get_font():
    default_profile = (
        popen(
            "gsettings get org.gnome.Terminal.ProfilesList default"
        )
        .read()
        .strip("' \n")
    )
    font = (
        popen(
            "gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{}/ font".format(
                default_profile
            )
        )
        .read()
        .strip("' \n")
    )
    return font
