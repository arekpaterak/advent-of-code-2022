from functools import cmp_to_key
from math import prod


def compare(left: int | list, right: int | list) -> int:
    match left, right:
        case int(), int():
            return (left > right) - (left < right)
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case list(), list():
            for (l, r) in zip(left, right):
                cmp = compare(l, r)
                if cmp != 0:
                    return cmp
            return compare(len(left), len(right))


# Read and process an input
test = False
filename = "input.txt" if not test else "example.txt"
with open(filename) as f:
    pairs = [[*map(eval, pair.split())] for pair in f.read().split("\n\n")]

# The 1st star
print(sum(i for i, pair in enumerate(pairs, 1) if compare(*pair) < 0))

# The 2nd star
packets = sorted(sum(pairs, [[2], [6]]), key=cmp_to_key(compare))
decoder_key = prod([i for i, packet in enumerate(packets, 1) if packet in [[2], [6]]])
print(decoder_key)
