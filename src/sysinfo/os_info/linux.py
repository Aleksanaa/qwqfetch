info_dict = {
    "name": "",
    "version": "",
    "codename": "",
    "full_name": "",
    # As you can see this is for Arch Linux!
    "no_version": False,
}

key_order = ["name", "version", "codename"]


def get_from_distro():
    try:
        import distro

        info_dict.update(
            {
                "name": distro.name(),
                "version": distro.version(),
                "codename": distro.codename(),
            }
        )
        if info_dict["version"] == "rolling" or "":
            info_dict["no_version"] = True
            info_dict["version"] = ""
        if info_dict["codename"] == "n/a" or "":
            info_dict["codename"] = ""
    except ImportError:
        pass


def get_from_os_release():
    try:
        os_release = open("/etc/os-release").readlines()
        for key in os_release:
            if "PRETTY_NAME" in key:
                full_name = key.split("=", 1)[1].strip('" \n')
                if full_name != "":
                    info_dict["full_name"] = full_name
                    break
            elif "NAME" in key:
                info_dict["name"] = key.split("=")[1].strip('" ')
            elif "VERSION_ID" in key:
                info_dict["version"] = key.split("=")[1].strip('" ')
            elif "VERSION_CODENAME" in key:
                info_dict["codename"] = key.split("=")[1].strip()
            elif "BUILD_ID=rolling" in key:
                info_dict["no_version"] = True

    except (FileNotFoundError, IndexError):
        pass


def get_from_lsb_release():
    try:
        from ...tools.command import RunCommand

        lsb_release = RunCommand("lsb_release -a").readlines()
        for key in lsb_release:
            if "Description:" in key:
                name = key.split(":")[1].strip()
                if name != "n/a":
                    info_dict["full_name"] = name
            if "Release:" in key:
                version = key.split(":")[1].strip()
                if version == "rolling":
                    info_dict["no_version"] = True
                else:
                    info_dict["version"] = version

    except IndexError:
        pass


# Because /etc/issue is highly modified in many distros
# I don't consider it appropriate to detect it.

for method in [get_from_distro, get_from_os_release, get_from_lsb_release]:
    if (
        (info_dict["full_name"] != "")
        or (info_dict["no_version"] and info_dict["name"] != "")
        or ("" not in [info_dict[key] for key in key_order])
    ):
        break
    method()

if info_dict["name"] == "":
    info_dict["name"] = "Unknown Linux"

if info_dict["full_name"] != "":
    info = info_dict["full_name"]
else:
    info = ""
    for key in key_order:  # get correct output order
        info = f"{info} {info_dict[key]}"
        info = info.strip()
