from __future__ import annotations


def get() -> dict[str, str]:
    from ...tools import get_parents
    from .corrections import correction_dict

    result = {}

    for name in get_parents():
        name = name.replace(".exe", "")
        if not (
            name.endswith("sh")
            or name.endswith("shell")
            or name.startswith("python")
            or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux", "cmd"]
        ):
            if name in correction_dict.keys():
                result["Terminal"] = correction_dict[name]
            elif name == "login":
                from os import getenv

                result["Terminal"] = f"tty{getenv('XDG_VTNR')}"
            else:
                result["Terminal"] = name
            break

    try:
        from importlib import import_module

        name = name.strip("-").replace("-", "_").replace(" ", "").lower()
        get_font = getattr(import_module(f".{name}", package=__package__), "get_font")

        result["Terminal Font"] = get_font().strip()
    except (ModuleNotFoundError, AttributeError):
        pass

    return result
