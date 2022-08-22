from ...tools import parse_info

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
        os_release = open("/etc/os-release").read()
        requirements = {
            "PRETTY_NAME": "full_name",
            "NAME": "name",
            "VERSION_ID": "version",
            "VERSION_CODENAME": "codename",
            "BUILD_ID": "build_id",
        }
        outputs: dict[str, str] = parse_info.parser(os_release, requirements, "=")
        if outputs.pop("build_id") == "rolling":
            info_dict["no_version"] = True
        for key in outputs.keys():
            if outputs[key] != "":
                info_dict[key] = outputs[key].strip('"')

    except (FileNotFoundError, IndexError):
        pass


def get_from_lsb_release():
    try:
        from ...tools.command import RunCommand

        requirements = {"Description": "full_name", "Release": "version"}
        lsb_release = RunCommand("lsb_release -a").read()
        lsb_release: dict[str, str] = parse_info.parser(lsb_release, requirements, ":")

        if lsb_release["full_name"] != "n/a" or "":
            info_dict["full_name"] = lsb_release["full_name"]
        if lsb_release["version"] == "rolling":
            info_dict["no_version"] = True
        elif lsb_release["version"]:
            info_dict["version"] = lsb_release["version"]

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

if not info_dict["name"]:
    info_dict["name"] = "Unknown Linux"

if info_dict["full_name"]:
    info = info_dict["full_name"]
else:
    info = ""
    for key in key_order:  # get correct output order
        info = f"{info} {info_dict[key]}"
        info = info.strip()
