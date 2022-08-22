from __future__ import annotations
from ...tools import get_parents, RunCommand

shell_name, shell_ver = "", ""

for name in get_parents():
    if name != "python.exe":
        shell_name = name.replace(".exe", "")
        break

if shell_name == "cmd":
    shell_ver = (
        RunCommand("cmd -ver").readline().split("[")[1].split()[-1].strip("]").strip()
    )

elif shell_name == "powershell" or "pwsh":
    command = "pwsh -Command" if shell_name == "pwsh" else "powershell"
    shell_ver = ".".join(
        [
            s
            for s in (
                RunCommand(f"{command} $PSVersionTable.PSVersion")
                .read()
                .split("\n")[2]
                .split()
            )
            if s
        ]
    )
    shell_ver = shell_ver.replace(".preview", "-preview")

elif shell_name == "bash":
    bash_path = "C:\\Program Files\\Git\\bin\\bash.exe"
    from os import getenv

    for path in getenv("PATH").split(";"):
        if path.endswith("Git\\cmd"):
            bash_path = path.replace("cmd", "bin\\bash.exe")
            break
    shell_ver = RunCommand(f"'{bash_path}' -c 'echo $BASH_VERSION'").read().strip()
