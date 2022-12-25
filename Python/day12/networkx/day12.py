import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class HeightMap:
    def __init__(self, data) -> None:
        self.grid = np.array(data)

        self.start = tuple(*np.argwhere(self.grid == 'S'))
        self.grid[self.start] = 'a'
        self.goal = tuple(*np.argwhere(self.grid == 'E'))
        self.grid[self.goal] = 'z'

        self.graph = nx.grid_2d_graph(*self.grid.shape, create_using=nx.DiGraph)
        self.graph.remove_edges_from([(a, b) for a, b in self.graph.edges if ord(self.grid[b]) - ord(self.grid[a]) > 1])

    def visualize(self):
        plt.imshow([[ord(height) for height in row] for row in self.grid])
        plt.show()

    def path_length(self, target):
        return nx.shortest_path_length(self.graph, target=target)


# Read and process an input
test = False
filename = "input.txt" if not test else "example.txt"
with open(filename) as f:
    data = [[*line.strip()] for line in f.readlines()]

map = HeightMap(data)
path_length = map.path_length(map.goal)

# The 1st star
print(path_length[map.start])

# The 2nd star
print(min(path_length[a] for a in path_length if map.grid[a] == 'a'))
