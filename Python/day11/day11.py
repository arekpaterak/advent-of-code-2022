from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Callable
import re


@dataclass
class Item:
    worry_level: int


class Monkey:
    monkeys: list[Monkey] = []

    @staticmethod
    def monkey_business() -> int:
        result = 1
        for monkey in sorted(Monkey.monkeys, key=lambda monkey: monkey.count, reverse=True)[:2]:
            result *= monkey.count
        return result

    def __init__(self, lines: list[str]) -> None:
        self.number: int = int(re.sub('\D', '', lines[0]))
        self.items: list[Item] = [Item(int(worry_level)) for worry_level in re.sub('\D', ' ', lines[1]).split()]
        self.operation: Callable = eval(f"lambda old: {re.sub('Operation: new = ', '', lines[2])}")
        self.test: Test = Test(lines[3:])
        self.count: int = 0

        self.monkeys.append(self)

    def __str__(self) -> str:
        return (
            f"Monkey {self.number}:\n  Starting items: "
            + ", ".join(str(item) for item in self.items)
            + "\n"
        )

    def turn(self) -> None:
        while self.items:
            item = self.inspect_item()
            # item.worry_level //= 3
            item.worry_level %= math.prod([test.divider for test in Test.tests])
            self.throw(item)

    def inspect_item(self) -> Item:
        item = self.items.pop(0)
        item.worry_level = self.operation(item.worry_level)
        self.count += 1
        return item

    def throw(self, item: Item) -> None:
        monkey = self.test(item)
        monkey.items.append(item)


class Test:
    tests: list[Test] = []

    def __init__(self, lines: list[str]) -> None:
        self.divider: int = int(re.sub('\D', '', lines[0]))
        self.if_true: int = int(re.sub('\D', '', lines[1]))
        self.if_false: int = int(re.sub('\D', '', lines[2]))

        self.tests.append(self)

    def __call__(self, item: Item) -> Monkey:
        if item.worry_level % self.divider == 0:
            return Monkey.monkeys[self.if_true]
        else:
            return Monkey.monkeys[self.if_false]


# Read and process an input
test = False
filename = "example.txt" if test else "input.txt"
with open(filename) as f:
    data = f.read().split("\n\n")

for part in data:
    lines = [line.strip() for line in part.split("\n")]
    monkey = Monkey(lines)

# The 2nd star
for _ in range(1, 10001):
    for monkey in Monkey.monkeys:
        monkey.turn()

print(Monkey.monkey_business())
