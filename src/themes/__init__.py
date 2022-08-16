from .. import globals
from .system_theme import theme, icons, cursor


def run():
    result_new = {"Theme": theme, "Icons": icons, "Cursor": cursor}
    globals.set({"result": result_new})
