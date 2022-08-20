from ...tools.command import RunCommand


def get_font():
    default_profile = (
        RunCommand("gsettings get org.gnome.Terminal.ProfilesList default")
        .read().strip("' \n")
    )
    font = (
        RunCommand(f"gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{default_profile}/ font")
        .read().strip("' \n")
    )
    return font
