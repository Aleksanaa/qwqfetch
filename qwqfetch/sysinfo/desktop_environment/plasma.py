from ...tools.command import RunCommand


def read_version(command: str, location: int):
    try:
        return RunCommand(command).read().split()[location].strip()
    except:
        return ""


def get():
    plasma_version = read_version("plasmashell --version", 1)
    kde_version = read_version("kded5 --version", 1)
    qt_version = read_version("qtpaths-qt5 --qt-version", 0)
    result = f"Plasma {plasma_version.strip()}"
    if kde_version:
        result += f" [KF5 {kde_version}]"
    if qt_version:
        result += f" [Qt {qt_version}]"
    return result
