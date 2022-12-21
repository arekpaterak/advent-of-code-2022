# Read file
filename = "input.txt"
data = open(filename).read().strip()
lines = [line for line in data.split("\n")]

# Split the data to a drawing of the starting stacks of crates and the rearrangement procedure
empty_line = lines.index("")
drawing = lines[:empty_line]
procedure = [line[5:] for line in lines[empty_line+1:]]

# Create and fill stacks with crates
number_of_stacks = int(drawing[-1][-2])
stacks = [[] for _ in range(number_of_stacks)]
for line in drawing[:-1]:
    for char1, char2 in zip(line, drawing[-1]):
        if char1.isalpha():
            crate = char1
            stacks[int(char2) - 1].insert(0, crate)

# Move crates according to the procedure
for step in procedure:
    moves, old, new = (int(i) for i in step.replace(" from ", ",").replace(" to ", ",").split(","))

    # The 1st star
    # for move in range(moves):
    #     stacks[new-1].append(stacks[old-1].pop())

    # The 2nd star
    crates_to_move = stacks[old-1][-moves:]
    del stacks[old-1][-moves:]
    stacks[new-1].extend(crates_to_move)

# Print the answer
for stack in stacks:
    print(stack[-1], end="")
