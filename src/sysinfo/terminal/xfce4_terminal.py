from os.path import expanduser
from ...tools import parse_info


def get_font():
    xfce4_config = f"{expanduser('~')}/.config/xfce4/terminal/terminalrc"
    needs = {"FontName": "font_name", "FontUseSystem": "use_system"}
    results = parse_info.parser(open(xfce4_config).read(), needs, "=")
    if "font_name" in results:
        return results["font_name"]
    elif "use_system" in results:
        from ...tools.command import run_command

        font_name = (
            run_command("gsettings get org.gnome.desktop.interface monospace-font-name")
            .read()
            .strip("'")
        )
        if font_name != "":
            return font_name
