def get(result):

    from ...tools import get_parents

    for name in get_parents():
        if not (
            name.endswith("sh")
            or name.endswith("shell")
            or name.startswith("python")
            or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux"]
        ):
            result["Terminal"] = name
            break

    try:
        from importlib import import_module

        name = name.replace("-", "_").replace(" ", "_")
        get_font = getattr(import_module(".{}".format(name), __package__), "get_font")
        
        result["Terminal Font"] = get_font().strip()
    except (ModuleNotFoundError, AttributeError):
        pass
