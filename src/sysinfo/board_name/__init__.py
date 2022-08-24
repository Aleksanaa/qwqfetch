from __future__ import annotations
from src.framework import Puzzle
from . import linux

def process(output:list):
    return {"Host":output[0]}

def get() -> dict[str, str]:
    return Puzzle('get_board_name',processor=process).solve()
