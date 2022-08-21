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

elif shell_name == "powershell":
    shell_ver = ".".join(
        [
            s
            for s in (
                RunCommand("powershell $PSVersionTable.PSVersion")
                .read()
                .split("\n")[2]
                .split()
            )
            if s
        ]
    )
