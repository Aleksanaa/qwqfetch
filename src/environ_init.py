from platform import system
from os import name as ostype
from src.framework import environ
import sys

# Don't put time-consuming code here!
def init():
    name = system()
    environ.sets(
        {
            "is_windows": name == "Windows",
            "is_linux": name == "Linux",
            "is_macos": name == "Darwin",
            "is_posix": ostype == "posix",
            "is_android": hasattr(sys, "getandroidapilevel"),
        }
    )
