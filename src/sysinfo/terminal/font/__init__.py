from importlib import import_module


def get_font_all(name: str) -> str:
    try:
        name = name.strip("-").replace("-", "_").replace(" ", "").lower()
        get_font = getattr(import_module(f".{name}", package=__name__), "get_font")

        return get_font().strip()
    except (ModuleNotFoundError, AttributeError):
        return ""
