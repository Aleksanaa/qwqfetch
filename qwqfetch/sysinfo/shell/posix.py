import os
from ...tools.command import RunCommand

shell_name = os.getenv("SHELL").split("/")[-1].strip()

if shell_name in ["bash", "zsh"]:
    shell_ver = RunCommand(f"{shell_name} -c 'echo ${shell_name.upper()}_VERSION'").read()
else:
    shell_ver = ""
