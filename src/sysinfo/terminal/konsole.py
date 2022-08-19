from os.path import expanduser


def get_font():
    home_path = expanduser("~")
    try:
        konsolerc = open("{}/.config/konsolerc".format(home_path)).readlines()
        for line in konsolerc:
            if line.startswith("DefaultProfile="):
                default_profile_name = line.split("=", 1)[1].strip()
                default_profile = open(
                    "{}/.local/share/konsole/{}".format(home_path, default_profile_name)
                ).readlines()
                for line in default_profile:
                    if line.startswith("Font="):
                        font_attr = line.split("=", 1)[1].split(",")
                        font_name = font_attr[0]
                        font_size = font_attr[1]
                        return "{} {}".format(font_name, font_size)

    except FileNotFoundError:
        pass
    return ""
