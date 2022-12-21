# Read file
filename = "input.txt"
with open(filename) as f:
    buffer = f.read().strip()

# The 1st star
number_of_distinct = 4
processed = []
for char in buffer:
    processed.append(char)
    if len(processed) >= number_of_distinct:
        if len(processed[-number_of_distinct:]) == len(set(processed[-number_of_distinct:])):
            break

# Print the answer
print(len(processed))

# The 2nd star
number_of_distinct = 14
processed = []
for char in buffer:
    processed.append(char)
    if len(processed) >= number_of_distinct:
        if len(processed[-number_of_distinct:]) == len(set(processed[-number_of_distinct:])):
            break

# Print the answer
print(len(processed))
