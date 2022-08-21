from __future__ import annotations
from ... import global_vars

sys_type = global_vars.get(["platform"])[0]["type"]


def get() -> dict[str, str]:
    if sys_type == "posix":
        from .posix import shell_name, shell_ver
    else:
        shell_name, shell_ver = "", ""

    return {'Shell': f"{shell_name} {shell_ver}".strip()}
