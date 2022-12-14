from os.path import expanduser
from ....tools import parse_info


def get_font() -> str:
    xfce4_config = f"{expanduser('~')}/.config/xfce4/terminal/terminalrc"
    needs = {"FontName": "font_name", "FontUseSystem": "use_system"}
    try:
        results = parse_info.parser(open(xfce4_config).read(), needs, "=")
        if results["use_system"] == "TRUE":
            from ....tools.command import run_command

            font_name = (
                run_command("gsettings get org.gnome.desktop.interface monospace-font-name")
                .read()
                .strip("'")
            )
            if font_name:
                return font_name

        else:
            return results["font_name"]
    except FileNotFoundError:
        pass