from ...tools.command import run_command


def read_version(command,location):
    try:
        return run_command(command).read().split()[location].strip()
    except:
        return ""

def get():
    plasma_version = read_version("plasmashell --version",1)
    kde_version = read_version("kded5 --version",1)
    qt_version = read_version("qtpaths-qt5 --qt-version",0)
    result = ("Plasma %s" %plasma_version).strip()
    if kde_version != "":
        result += " [KF5 %s]" %kde_version
    if qt_version != "":
        result += " [Qt %s]" %qt_version
    return result


    
