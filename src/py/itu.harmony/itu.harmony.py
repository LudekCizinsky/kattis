from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph
from itu.algs4.stdlib.instream import InStream
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.graphs.edge import Edge


class CanBe2Colored:

    def __init__(self, G, s):
        # Define the properties
        self.G = G
        self.s = s
        self.visited = dict()
        self.can_be_colored = 1

        # Find out whether all components of Graph can be color coded
        for vertex in range(self.G.V()):
            if vertex not in self.visited:
                response = self.can_be_colored_bfs(vertex)
                if response == 0:
                    break

        print(self.can_be_colored)

    def can_be_colored_bfs(self, s):
        """
        Finds out whether the given component of the graph can be color coded according to defined rules.
        :s: start node
        :G: Graph object
        DISCLAIMER: My code builds on top of the following source:
        https://github.com/itu-algorithms/itu.algs4/blob/master/itu/algs4/graphs/breadth_first_paths.py
        All credits therefore goes to these authors.
        :return: 1 if can be colored, 0 if not
        """

        # Setup queue for nodes to explore
        queue = Queue()

        # Setup a symbol table with initial nodes and its color
        self.visited[s] = "red"

        # Add the initial node
        queue.enqueue(s)

        # Iterate until you have not visited all the nodes within the given component
        while not queue.is_empty():

            # Get the node to be explored from the queue
            v = queue.dequeue()

            # Iterate over the neighbors of the node
            for edge in self.G.adj(v):

                # From the edge, get the other node and whether the edge is conflict (or harmony)
                w = edge.other(v)
                is_conflict = edge.weight() == 1

                # Do the proper color labeling and add it to the queue
                if w not in self.visited:

                    # Label as visited and assign appropriate color
                    color_other = self.visited[v]

                    # Edge is conflict - colors must be opposite
                    if is_conflict:
                        if color_other == "red":
                            self.visited[w] = "orange"
                        else:
                            self.visited[w] = "red"

                    # Edge is harmony, colors must be same
                    else:
                        self.visited[w] = color_other

                    # Add it to the nodes that has to be explored
                    queue.enqueue(w)

                # Check that conditions are met
                else:

                    # Get color of the other node
                    color_other = self.visited[v]

                    # Conflict: If nodes have the same color --> there is problem --> return 0
                    if is_conflict:

                        # Conditions not met --> return
                        if color_other == self.visited[w]:
                            self.can_be_colored = 0
                            return 0

                    # Harmony: If nodes do NOT have the same color –> there is a problem --> return 0
                    else:
                        if color_other != self.visited[w]:
                            self.can_be_colored = 0
                            return 0

        # No problem --> return 1
        return 1


def main():

    # Get number of vertices and edges
    n, m = input().split(' ')

    # Build graph
    G = EdgeWeightedGraph(int(n))

    # Add adges to graph
    for _ in range(int(m)):

        # Get edge components
        v, w, weight = input().split(' ')

        # Build the edge
        e = Edge(int(v), int(w), int(weight))

        # Add the edge
        G.add_edge(e)

    # Run the BFS to find out the result
    CanBe2Colored(G, 0)


if __name__ == "__main__":
    main()
