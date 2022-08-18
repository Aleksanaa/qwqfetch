import subprocess
from .pm_list import package_managers
import os
from sys import stdout


def check_command_exist(command):
    program = command.split()[0]
    paths = os.getenv("PATH").split(":")
    for path in paths:
        if os.path.isfile("%s/%s" % (path, program)):
            return True
    return False

def get(result):
# get the encoding of current terminal
    encoding = stdout.encoding

    packages_list = {}

    for pm in package_managers:
        if "command" in pm.keys():
            command = pm["command"]
            if check_command_exist(command):
                command_result = subprocess.run(command.split(), capture_output=True)
                if command_result.returncode == 0:
                    count = str(command_result.stdout,encoding).count('\n')
                    if count != 0:
                        packages_list[pm["name"]] = count

    packages_str = ""

    for pm, count in packages_list.items():
        packages_str += "%d (%s), " % (count, pm)

    packages_str = packages_str.strip(", ")
    result['Packages'] = packages_str
