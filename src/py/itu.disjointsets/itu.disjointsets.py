from sys import stdin


class WeightedUnionFind:

    def __init__(self, n):
        self.C = [i for i in range(n)]  # Start with creating singletons
        self.node_count = [1 for i in range(n)]
        self.node_children = [[] for _ in range(n)]

    def find_root(self, x):
        if x == self.C[x]:
            return x
        else:
            return self.find_root(self.C[x])

    def weighted_union(self, S, T):

        if S == T:
            return

        if self.node_count[S] <= self.node_count[T]:
            self.node_count[T] += self.node_count[S]
            self.C[S] = T
            self.node_children[T].append(S)
        else:
            self.node_count[S] += self.node_count[T]
            self.C[T] = S
            self.node_children[S].append(T)

    def move_item(self, S, T, s, t):

        if S == T:
            return

        # s is a root, i.e., precisely s == S
        if S == s:

            # Get all children of s first
            all_children = self.node_children[s]

            # The root has more than 1 child:
            # -- Changes in S
            # - Select new root: 1. first child in the list OR 2. Largest child OR ...
            # - Set new parent to child nodes
            # - Set new children to new root
            # - Increase size of root by size of new children
            # - Set size of node s to 1 and increase size of T by 1
            if len(all_children) > 1:
                # Changes in S
                new_root = all_children.pop()  # always last item
                self.C[new_root] = new_root
                append = self.node_children[new_root].append
                for child in all_children:
                    self.node_count[new_root] += self.node_count[child]
                    self.C[child] = new_root
                    append(child)

            # The root has only one child:
            # -- Changes in S
            # - set the child to be its own parent, i.e., the child is now root
            elif len(all_children) == 1:
                new_root = all_children[0]
                self.C[new_root] = new_root

        # s is NOT a root
        else:
            # Remove s from children of its parent
            self.node_children[self.C[s]].remove(s)
            self.node_count[S] -= 1

            # Change parent for s children
            append = self.node_children[S].append
            for child in self.node_children[s]:
                self.C[child] = S
                append(child)

        # Change count
        self.node_count[s] = 1
        self.node_count[T] += 1

        # Changes in T (common - no matter number of children or whether s is root or not)
        self.node_children[s] = []
        self.C[s] = T
        self.node_children[T].append(s)


def main():

    # Parse input
    n, _ = [int(i) for i in input().split()]

    # Create weighetd union find instance
    WUF = WeightedUnionFind(n)

    for line in stdin:
        operation, s, t = [int(item) for item in line.split()]
        S, T = WUF.find_root(s), WUF.find_root(t)
        # Query
        if operation == 0:
            if S == T:
                print(1)
            else:
                print(0)
        # Union
        elif operation == 1:
            WUF.weighted_union(S, T)

        # Move
        elif operation == 2:
            WUF.move_item(S, T, s, t)


if __name__ == '__main__':
    main()
