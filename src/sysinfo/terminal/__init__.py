def get(result):

    from ...tools import get_parents
    from .corrections import correction_dict

    for name in get_parents():
        if not (
            name.endswith("sh")
            or name.endswith("shell")
            or name.startswith("python")
            or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux"]
        ):
            if name in correction_dict.keys():
                result["Terminal"] = correction_dict[name]
            else:
                result["Terminal"] = name
            break

    try:
        from importlib import import_module

        name = name.strip("-").replace("-", "_").replace(" ", "").lower()
        get_font = getattr(
            import_module(".{}".format(name), package=__package__), "get_font"
        )

        result["Terminal Font"] = get_font().strip()
    except (ModuleNotFoundError, AttributeError):
        pass
