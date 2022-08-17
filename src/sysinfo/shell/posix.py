from os import getenv, popen

shell_name = getenv("SHELL").split("/")[-1].strip()

if shell_name in ["bash", "zsh"]:
    shell_ver = popen(
        "%s -c 'echo $%s_VERSION'" % (shell_name, shell_name.upper())
    ).read()
else:
    shell_ver = ""
