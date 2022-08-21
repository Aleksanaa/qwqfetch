from ... import globals

sys_type = globals.get(["platform"])[0]["type"]


def get() -> dict[str, str]:
    if sys_type == "posix":
        from .posix import shell_name, shell_ver
    else:
        shell_name, shell_ver = "", ""

    return {'Shell': f"{shell_name} {shell_ver}".strip()}
