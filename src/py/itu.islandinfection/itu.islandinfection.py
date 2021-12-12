from collections import deque


class World:

    def __init__(self, R, C):
        self.R = R
        self.C = C

        # Store world as a 2D array
        self.world = []

        # Position of Virus
        self.virus_pos = None

        # Define constants
        self.WATER = 0
        self.LAND = 1
        self.VIRUS = 2
        self.HUMAN = 3

        # Define directions: Down, left, up, right
        self.DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def load_world(self):

        for r in range(self.R):

            row_raw = input()
            row = []
            c = 0
            for val in row_raw:
                val = int(val)
                # Get Virus position
                if val == self.VIRUS:
                    self.virus_pos = (r, c)

                # Add value to row
                row.append(val)

                # Add column count
                c += 1

            # Add row to world
            self.world.append(row)

    def show_world(self):
        for row in self.world:
            print(row)

    def is_within_bounds(self, position):

        r, c = position  # row, column

        # Row wise
        if r < 0 or r >= self.R:
            return False

        # Column wise
        if c < 0 or c >= self.C:
            return False

        return True

    def isHumanInfected(self):

        # Start at virus position
        queue = deque()
        queue.append(self.virus_pos)

        # Keep of visited
        visited = set()

        # Do BFS through the world and try to reach human
        while queue:

            # Get the current position
            r, c = queue.popleft()

            # Browse only unvisited relevant places
            if (r, c) not in visited:

                # Label as visited
                visited.add((r, c))

                # Explore the neighbors
                for direction in self.DIRECTIONS:

                    # Get the coordinates of neighbor
                    r_nb, c_nb = r + direction[0], c + direction[1]

                    # Conduct an action based on neighbors kind
                    if self.is_within_bounds([r_nb, c_nb]):

                        # Land
                        if self.world[r_nb][c_nb] == self.LAND:
                            queue.append([r_nb, c_nb])

                        # Human
                        elif self.world[r_nb][c_nb] == self.HUMAN:
                            return 1

        return 0


def main():

    # Get number of rows and columns
    R, C = [int(item) for item in input().split(" ")]

    # Build the world
    world = World(R, C)
    world.load_world()

    # Find out whether human is infected
    print(world.isHumanInfected())


if __name__ == "__main__":
    main()
