import numpy as np

# Read and process an input
filename = "input.txt"
with open(filename) as f:
    motions = [line.strip() for line in f.readlines()]

move = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}

# The 1st star
head = 0 + 0j
tail = 0 + 0j
visited = set()
visited.add(tail)

for motion in motions:
    direction, steps = motion.split()
    for step in range(int(steps)):
        head += move[direction]
        distance = head - tail
        if abs(distance) >= 2:
            tail += complex(np.sign(distance.real), np.sign(distance.imag))
            visited.add(tail)
print(len(visited))

# The 2nd star
rope = [0 + 0j for _ in range(10)]
visited = set()
visited.add(rope[9])
for motion in motions:
    direction, steps = motion.split()
    for step in range(int(steps)):
        rope[0] += move[direction]
        for i in range(1, 10):
            distance = rope[i-1] - rope[i]
            if abs(distance) >= 2:
                rope[i] += complex(np.sign(distance.real), np.sign(distance.imag))
            visited.add(rope[9])
print(len(visited))
