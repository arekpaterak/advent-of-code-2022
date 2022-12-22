from __future__ import annotations
from dataclasses import dataclass


@dataclass
class File:
    size: int


class Directory:
    def __init__(self) -> None:
        self.name: str = ""
        self.files: list[File] = []
        self.directories: list[Directory] = []
        self.parent: None | Directory = None

    def size(self):
        return sum([file.size for file in self.files]) + sum([d.size() for d in self.directories])


# Read and process input
filename = "input.txt"
with open(filename) as f:
    data = f.read().strip()
lines = [line for line in data.split("\n")]



# The 1st star


# The 2nd star

