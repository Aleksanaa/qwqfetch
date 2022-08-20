from ...tools.command import RunCommand
from .pm_list import package_managers


def get(result):
    packages_list = {}

    for pm in package_managers:
        if "command" in pm.keys():
            output = RunCommand(pm["command"]).read()
            count = output.count("\n")
            if count != 0:
                packages_list[pm["name"]] = count

    packages = [f"{count} ({pm})" for pm, count in packages_list.items()]
    result["Packages"] = ', '.join(packages)
