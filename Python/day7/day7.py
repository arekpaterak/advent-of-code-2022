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

    def size(self) -> int:
        return sum([file.size for file in self.files]) + sum([d.size() for d in self.directories])


# Read and process an input
filename = "input.txt"
with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]

directories = []
current = None
for line in lines:
    # Going in
    if "$ cd" in line and ".." not in line:
        dir = Directory()
        dir.name = line.split(" ")[2]
        dir.parent = current

        directories.append(dir)

        if dir.parent:
            dir.parent.directories.append(dir)

        current = dir

    # Going out
    elif "$ cd .." in line:
        current = current.parent

    # Encountering a file
    elif line[0].isdecimal():
        size = int(line.split(" ")[0])
        current.files.append(File(size))

# The 1st star
size_limit = 100000
print(sum([dir.size() for dir in directories if (dir.size() <= size_limit)]))

# The 2nd star
disk_space = 70000000
needed_space = 30000000
unused_space = disk_space - directories[0].size()
to_delete = [dir for dir in directories if (unused_space + dir.size() > needed_space)]
print(min(to_delete, key=lambda x: x.size()).size())
