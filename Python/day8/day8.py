from dataclasses import dataclass
import numpy as np


@dataclass
class Tree:
    i: int
    j: int
    height: int

    def is_visible(self) -> bool:

        return all(tree.height < self.height for tree in trees[self.i, :self.j]) or \
               all(tree.height < self.height for tree in trees[self.i, self.j+1:]) or \
               all(tree.height < self.height for tree in trees[:self.i, self.j]) or \
               all(tree.height < self.height for tree in trees[self.i+1:, self.j])

    def viewing_distance(self, direction: str) -> int:
        distance = 0
        match direction:
            case "left":
                for tree in reversed(trees[self.i, :self.j]):
                    if tree.height <= self.height:
                        distance += 1
                    if tree.height >= self.height:
                        break
            case "right":
                for tree in trees[self.i, self.j+1:]:
                    if tree.height <= self.height:
                        distance += 1
                    if tree.height >= self.height:
                        break
            case "up":
                for tree in reversed(trees[:self.i, self.j]):
                    if tree.height <= self.height:
                        distance += 1
                    if tree.height >= self.height:
                        break
            case "down":
                for tree in trees[self.i+1:, self.j]:
                    if tree.height <= self.height:
                        distance += 1
                    if tree.height >= self.height:
                        break
        return distance

    def scenic_score(self) -> int:
        return self.viewing_distance("left")*self.viewing_distance("right")*self.viewing_distance("up")*self.viewing_distance("down")


# Read and process input
filename = "input.txt"
with open(filename) as f:
    data = f.read().strip()
lines = [line for line in data.split("\n")]

trees = np.array([[Tree(i, j, int(height)) for j, height in enumerate(line)] for i, line in enumerate(lines)])

# The 1st star
visible = 0
for row in trees:
    for tree in row:
        if tree.is_visible():
            visible += 1
print(visible)

# The 2nd star
highest_scenic_score = 0
for row in trees:
    for tree in row:
        if tree.scenic_score() > highest_scenic_score:
            highest_scenic_score = tree.scenic_score()
print(highest_scenic_score)
