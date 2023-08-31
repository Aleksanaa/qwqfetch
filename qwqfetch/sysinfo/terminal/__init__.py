from __future__ import annotations
from .font import get_font_all
from ... import global_vars


def get() -> dict[str, str]:
    from ...tools import get_parents
    from .corrections import correction_dict

    sys_name = global_vars.get(["platform"])[0]["name"]

    result = {}

    for name in get_parents():
        name = name.replace(".exe", "")
        if not (
            name.endswith("sh")
            or name.endswith("shell")
            or name.startswith("python")
            or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux", "cmd"]
        ):
            if sys_name == "Darwin" and name == "Terminal":
                name = "Apple Terminal"
            if name in correction_dict.keys():
                result["Terminal"] = correction_dict[name]
            elif name == "login":
                # macos's default terminal starts a progress called login
                if sys_name == "Darwin":
                    continue
                from os import getenv

                result["Terminal"] = f"tty{getenv('XDG_VTNR')}"
            else:
                result["Terminal"] = name
            break

    result["Terminal Font"] = get_font_all(name)

    return result
