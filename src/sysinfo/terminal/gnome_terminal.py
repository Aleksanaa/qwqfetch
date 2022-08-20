from ...tools.command import run_command


def get_font():
    default_profile = (
        run_command("gsettings get org.gnome.Terminal.ProfilesList default")
        .read()
        .strip("' \n")
    )
    font = (
        run_command(
            "gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{}/ font".format(
                default_profile
            )
        )
        .read()
        .strip("' \n")
    )
    return font
