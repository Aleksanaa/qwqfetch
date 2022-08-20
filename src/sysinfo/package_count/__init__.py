from ...tools.command import run_command
from .pm_list import package_managers


def get(result):

    packages_list = {}

    for pm in package_managers:
        if "command" in pm.keys():
            output = run_command(pm["command"]).read()
            count = output.count("\n")
            if count != 0:
                packages_list[pm["name"]] = count

    packages_str = ""

    for pm, count in packages_list.items():
        packages_str += "%d (%s), " % (count, pm)

    packages_str = packages_str.strip(", ")
    result["Packages"] = packages_str
