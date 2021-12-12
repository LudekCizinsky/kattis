

"""
My solution got inspired from the following source:
https://github.com/rvrheenen/OpenKattis/blob/master/Python/coast/coast.py,
however, I wrote the code by myself.
"""


class World:

    def __init__(self, N, M):

        # Assume that the world is surrounded by sea
        self.N = N + 2
        self.M = M + 2
        self.coast_len = 0

        # This will be a 2D array representing the grid
        self.world = []

        # This will be for BFS to keep track of progress
        self.visited = [[False]*self.M for _ in range(self.N)]

        # Define constants
        self.WATER = 0
        self.LAND = 1

        # Down, left, up, right
        self.DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def load_world(self):

        # Add first row of ocean
        self.world.append([0 for _ in range(self.M)])

        # Add the rows between the first and last one
        for _ in range(self.N - 2):
            row = [self.WATER] + [int(item)
                                  for item in list(input())] + [self.WATER]
            self.world.append(row)

        # Add last row
        self.world.append([0 for _ in range(self.M)])

    def show_world(self):
        for row in self.world:
            print(row)

    def is_within_bounds(self, position):

        n, m = position

        # Row wise
        if n < 0 or n >= self.N:
            return False

        # Column wise
        if m < 0 or m >= self.M:
            return False

        return True

    def count_coast_len(self):

        # Start at top left corner
        queue = list()
        queue.append([0, 0])

        # Do BFS through the world and count the coastal len
        while queue:

            # Get the current position
            n, m = queue.pop(0)

            # Browse only unvisited water
            if self.world[n][m] == self.WATER and not self.visited[n][m]:

                # Label as visited
                self.visited[n][m] = True

                # Explore the neighbors
                for direction in self.DIRECTIONS:

                    # Get the coordinates of neighbor
                    n_nb, m_nb = n + direction[0], m + direction[1]

                    # Conduct an action based on neighbors kind
                    if self.is_within_bounds([n_nb, m_nb]):

                        # Water -> add to queue
                        if self.world[n_nb][m_nb] == self.WATER:
                            queue.append([n_nb, m_nb])

                        # Land -> increase coastal line
                        else:
                            self.coast_len += 1

        return self.coast_len


def main():

    # Load N, M
    N, M = [int(item) for item in input().split(" ")]

    # Build a world
    world = World(N, M)
    world.load_world()

    # Iterate over the sea and count coastal
    # length whenever you encounter a land
    result = world.count_coast_len()
    print(result)


if __name__ == "__main__":
    main()
