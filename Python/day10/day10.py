import numpy as np


class ClockCircuit:
    def __init__(self) -> None:
        self.cycle: int = 1
        self.register: int = 1
        self.queue: list = []

    def addx(self, value: int) -> None:
        self.queue.extend([0, value])

    def noop(self) -> None:
        self.queue.extend([0])

    def execute(self) -> None:
        self.cycle += 1
        self.register += self.queue.pop(0)

    def signal_strength(self) -> int:
        return self.cycle * self.register


class Screen:
    width: int = 40
    height: int = 6

    def __init__(self) -> None:
        self.pixels = []
        self.sprite_position = ['#', '#', '#']

    def display(self) -> None:
        for row in np.reshape(self.pixels, (self.height, self.width)):
            for char in row:
                print(char, end="")
            print("\n")


# Read and process an input
filename = "input.txt"
with open(filename) as f:
    instructions = [line.split() for line in f.readlines()]

# The 1st and 2nd star
clock_circuit = ClockCircuit()
screen = Screen()
cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = []
while clock_circuit.cycle <= 240:
    if instructions:
        instruction = instructions.pop(0)
        if len(instruction) == 2:
            V = int(instruction[1])
            clock_circuit.addx(V)
        else:
            clock_circuit.noop()

    if clock_circuit.cycle in cycles:
        signal_strengths.append(clock_circuit.signal_strength())

    if len(screen.sprite_position) <= (clock_circuit.cycle - 1) % 40:
        screen.pixels.append('.')
    elif screen.sprite_position[(clock_circuit.cycle - 1) % 40] == '#':
        screen.pixels.append('#')
    else:
        screen.pixels.append('.')

    clock_circuit.execute()
    screen.sprite_position = ['.' for _ in range(clock_circuit.register - 1)] + ['#', '#', '#']

print(sum(signal_strengths))
screen.display()
