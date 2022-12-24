import numpy as np

position_to_elevation = {'S': 'a', 'E': 'z'}

# Read and process an input
test = False
filename = "input.txt" if not test else "example.txt"
with open(filename) as f:
    lines = f.readlines()

steps = 0