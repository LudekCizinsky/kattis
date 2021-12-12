
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.graphs.directed_edge import DirectedEdge


def main():

    # Load height
    h = int(input())
    V = int(((h + 1)*(h + 2))/2)

    # Build graph
    G = EdgeWeightedDigraph(V)

    weights = list()
    for parent in range(V):
        level = 0
        if not weights:
            weights = [int(item) for item in input().split(" ")]
            level += 1

        for i in range(2):
            child = parent + level + i
            print(parent, child)
            w = weights.pop()
            e = DirectedEdge(parent, child, w)
            G.add_edge(e)
        print()


if __name__ == "__main__":
    main()
