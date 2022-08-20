from os import getenv
from ...tools.command import run_command

shell_name = getenv("SHELL").split("/")[-1].strip()

if shell_name in ["bash", "zsh"]:
    shell_ver = run_command(
        "%s -c 'echo $%s_VERSION'" % (shell_name, shell_name.upper())
    ).read()
else:
    shell_ver = ""
