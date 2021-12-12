
from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph
from itu.algs4.graphs.edge import Edge
from itu.algs4.graphs.kruskal_mst import KruskalMST
from itu.algs4.sorting.min_pq import MinPQ


class newEdge:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y


def showMST(mst):

    edges = mst.edges()
    min_pq = MinPQ(len(edges))
    for edge in edges:

        x = edge.either()
        y = edge.other(edge.either())

        if x < y:
            new_edge = newEdge(x, y)
        else:
            new_edge = newEdge(y, x)

        min_pq.insert(new_edge)

    print(mst.weight())
    while not min_pq.is_empty():
        e = min_pq.del_min()
        print(f"{e.x} {e.y}")


def isThereMST(n, m):

    G = EdgeWeightedGraph(n)
    for _ in range(m):
        u, v, w = [int(item) for item in input().split(" ")]
        e = Edge(u, v, w)
        G.add_edge(e)
    mst = KruskalMST(G)

    if len(mst.edges()) != (n - 1):
        print("Impossible")
    else:
        showMST(mst)


def main():

    while True:

        n, m = [int(item) for item in input().split(" ")]

        if n == 0 and m == 0:
            break
        else:
            isThereMST(n, m)


if __name__ == "__main__":

    main()
