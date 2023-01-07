import matplotlib.pyplot as plt


class SandSimulator:
    def __init__(self, scan) -> None:
        self.rocks = set()
        for path in scan:
            points = [complex(*tuple(int(coordinate) for coordinate in coordinates.split(","))) for coordinates in
                      path.split(" -> ")]
            for pair in zip(points, points[1:]):
                point1, point2 = pair
                if point1.real == point2.real:
                    start, end = min(point1.imag, point2.imag), max(point1.imag, point2.imag)
                    self.rocks |= {complex(point1.real, b) for b in range(int(start), int(end + 1))}
                else:
                    start, end = min(point1.real, point2.real), max(point1.real, point2.real)
                    self.rocks |= {complex(a, point1.imag) for a in range(int(start), int(end + 1))}

        self.floor = max(rock.imag for rock in self.rocks) + 2

        self.source_of_sand = complex(500, 0)
        self.rested_sand = set()

    def visualize(self):
        def show(tiles, marker):
            x = [tile.real for tile in tiles]
            y = [tile.imag for tile in tiles]
            plt.scatter(x, y, marker=marker)

        show(self.rocks, marker="s")
        show(self.rested_sand, marker="o")
        plt.gca().invert_yaxis()
        plt.show()

    def generate_sand(self, abyss=False):
        path = [self.source_of_sand]
        while True:
            position = path[-1]
            for tile in position+1j, position-1+1j, position+1+1j:
                if tile not in (self.rocks | self.rested_sand) and tile.imag < self.floor:
                    path.append(tile)
                    break
            else:
                if position == self.source_of_sand:
                    self.rested_sand.add(position)
                    return
                elif abyss and position.imag > simulator.floor-2:
                    return
                self.rested_sand.add(position)
                del path[-1]


# Read and process an input
test = True
filename = "example.txt" if test else "input.txt"
with open(filename) as f:
    scan = [line.strip() for line in f.readlines()]

simulator = SandSimulator(scan)
simulator.generate_sand(abyss=True)
simulator.visualize()
print(len(simulator.rested_sand))

simulator.generate_sand()
simulator.visualize()
print(len(simulator.rested_sand))
