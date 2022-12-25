import numpy as np


class HeightMap:
    def __init__(self, data) -> None:
        self.grid = np.array(data)

        self.start = tuple(*np.argwhere(self.grid == 'S'))
        self.grid[self.start] = 'a'
        self.goal = tuple(*np.argwhere(self.grid == 'E'))
        self.grid[self.goal] = 'z'

    def BFS(self, start, reverse=False):
        def adjacent(position):
            result = []
            candidates = [(position[0]-1, position[1]), (position[0], position[1]+1), (position[0]+1, position[1]), (position[0], position[1]-1)]
            for a in candidates:
                if not (a[0] < 0 or a[1] < 0 or a[0] >= visited.shape[0] or a[1] >= visited.shape[1]):
                    result.append(a)
            return result

        visited = np.array([[False for _ in row] for row in self.grid])
        queue = []
        distance = {}

        visited[start] = True
        queue.append(start)
        distance[start] = 0

        while queue:
            position = queue.pop(0)
            for a in adjacent(position):
                if not visited[a]:
                    if not reverse:
                        if ord(self.grid[a]) - ord(self.grid[position]) <= 1:
                            queue.append(a)
                            visited[a] = True
                            distance[a] = distance[position]+1
                    else:
                        if ord(self.grid[position]) - ord(self.grid[a]) <= 1:
                            queue.append(a)
                            visited[a] = True
                            distance[a] = distance[position]+1

        return distance


# Read and process an input
test = False
filename = "input.txt" if not test else "example.txt"
with open(filename) as f:
    data = [list(line.strip()) for line in f.readlines()]

map = HeightMap(data)

# The 1st star
path_length = map.BFS(map.start)
print(path_length[map.goal])

# The 2nd star
path_length = map.BFS(map.goal, reverse=True)
print(min(path_length[a] for a in path_length if map.grid[a] == 'a'))
