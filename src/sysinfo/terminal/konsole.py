from os.path import expanduser


def get_font() -> str:
    home_path = expanduser("~")
    try:
        konsolerc = open(f"{home_path}/.config/konsolerc").readlines()
        for line in konsolerc:
            if line.startswith("DefaultProfile="):
                default_profile_name = line.split("=", 1)[1].strip()
                default_profile = open(f"{home_path}/.local/share/konsole/{default_profile_name}").readlines()
                for line in default_profile:
                    if line.startswith("Font="):
                        font_attr = line.split("=", 1)[1].split(",")
                        font_name = font_attr[0]
                        font_size = font_attr[1]
                        return f"{font_name} {font_size}"

    except FileNotFoundError:
        pass
    return ""
