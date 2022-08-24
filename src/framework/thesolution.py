from __future__ import annotations
from types import FunctionType
from copy import deepcopy
from functools import wraps
from dataclasses import dataclass
from os import cpu_count
from multiprocessing.pool import ThreadPool


def solution(name: str, priority: int, condition: bool):
    def append(function: FunctionType):
        @wraps(function)
        def solution_wrap(*args, **kwargs):
            if condition:
                try:
                    return function(*args, **kwargs)
                except:
                    pass

        pool.add_solution(name, priority, solution_wrap)
        return solution_wrap

    return append


@dataclass
class Puzzle:

    name: str
    args: list = []
    kwargs: dict = {}
    checker: FunctionType = lambda v: True
    processor: FunctionType = lambda v: v

    def solve(self) -> None:
        return pool.solve(self)


class Pool:
    def __init__(self) -> None:
        self.__container = {"solutions": {}, "cache": {}}

    def __store(self, type: str, name: str, content):
        bookcase = self.__container[type]
        if not (name in bookcase and isinstance(bookcase[name], list)):
            bookcase[name] = []
        bookcase[name].append(content)

    def add_solution(self, name: str, priority: int, function: FunctionType) -> None:
        self.__store("solutions", name, {"priority": priority, "function": function})
        self.__container["solutions"][name] = sorted(
            self.__container["solutions"][name],
            key=lambda d: d["priority"],
            reverse=True,
        )

    def __store_return(self, name: str, content) -> list:
        self.__store("cache", name, content)
        return self.__container["cache"][name]

    def solve(self, puzzle: Puzzle):
        for solution in self.__container["solutions"][puzzle.name]:
            function = solution["function"]
            value = self.__store_return(
                puzzle.name, function(*puzzle.args, **puzzle.kwargs)
            )
            if value[-1] and puzzle.checker(deepcopy(value)) == True:
                return puzzle.processor(value)

    def psolve(self, puzzles: list[Puzzle]):
        return ThreadPool(cpu_count()).map(self.solve, puzzles)

if "pool" not in globals():
    pool = Pool()
psolve = pool.psolve
