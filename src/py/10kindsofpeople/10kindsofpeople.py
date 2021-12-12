
class World:

    def __init__(self, R, C):
        self.R = R
        self.C = C

        # Store world as a 2D array
        self.world = []

        # Define constants
        self.BINARY = 0
        self.DECIMAL = 1

        # Define directions: Down, left, up, right
        self.DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def load_world(self):

        for _ in range(self.R):
            row = [int(item) for item in list(input())]
            self.world.append(row)

    def show_world(self):
        for row in self.world:
            print(row)

    def colorMap(self):

        color = 2
        for r in range(self.R):
            for c in range(self.C):
                if self.world[r][c] in [0, 1]:

                    # get the needed input
                    KIND = self.world[r][c]
                    CURRENT = (r, c)

                    # Adjust the color
                    if KIND == self.BINARY:
                        color_adj = "B" + str(color)
                    else:
                        color_adj = "D" + str(color)

                    self.buildArea(KIND, CURRENT, COLOR=color_adj)
                    color += 1

    def is_within_bounds(self, position):

        n, m = position

        # Row wise
        if n < 0 or n >= self.R:
            return False

        # Column wise
        if m < 0 or m >= self.C:
            return False

        return True

    def from2Dto1D(self, pos):

        r, c = pos
        return r*self.C + c

    def buildArea(self, KIND, CURRENT, COLOR):

        # Parse current location and put it to the queue
        queue = list()
        queue.append(CURRENT)

        # Do BFS through the world and build the available area
        while queue:

            # Get the current position
            r, c = queue.pop(0)

            # Browse only unvisited relevant places
            if self.world[r][c] == KIND:

                # Label as visited
                self.world[r][c] = COLOR

                # Explore the neighbors
                for direction in self.DIRECTIONS:

                    # Get the coordinates of neighbor
                    r_nb, c_nb = r + direction[0], c + direction[1]

                    # Conduct an action based on neighbors kind
                    if self.is_within_bounds([r_nb, c_nb]):

                        # Same kind -> add to queue
                        if self.world[r_nb][c_nb] == KIND:
                            queue.append([r_nb, c_nb])


def main():

    # Read the first line defining the world
    R, C = [int(value) for value in input().split(" ")]

    # Build the world
    world = World(R, C)
    world.load_world()

    # Color map
    world.colorMap()

    # Process N queries
    N = int(input())
    for _ in range(N):

        # Load query and convert it to 0-based indices
        r1, c1, r2, c2 = [int(value) - 1 for value in input().split(" ")]

        # Show the result
        if world.world[r1][c1] == world.world[r2][c2]:

            # Parse kind
            KIND = list(world.world[r1][c1])[0]

            # Binary
            if KIND == "B":
                print("binary")

            # Decimal
            else:
                print("decimal")
        else:
            print("neither")


if __name__ == "__main__":
    main()
