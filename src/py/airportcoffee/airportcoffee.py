class Node:

    def __init__(self, order, decision_path) -> None:
        self.order = order
        self.decision_path = decision_path
        self.total_time = 0
        self.waiting_distance = 0
        self.fast_distance = 0  # Distance she has left from previous walk when she drinks coffee
        self.left = None
        self.right = None

    def decide(self):

        # Distance to the next
        if self.order == (n - 1):
            distance = l - stands[self.order]
        else:
            distance = stands[self.order + 1] - stands[self.order]

        # Make the decision: Drink or not
        # * No drink
        no_drink = Node(self.order + 1, self.decision_path + [False])
        slow, fast, fast_left, waiting_left = self.no_drink_info(distance)
        no_drink.total_time = self.total_time + slow/a + fast/b
        no_drink.fast_distance = fast_left
        no_drink.waiting_distance = waiting_left
        self.right = no_drink

        # * Drink
        drink = Node(self.order + 1, self.decision_path + [True])
        slow, fast, fast_left, waiting_left = self.drink_info(distance)
        drink.total_time = self.total_time + slow/a + fast/b
        drink.fast_distance = fast_left
        drink.waiting_distance = waiting_left
        self.left = drink

        # Base case
        if self.order + 1 < n:
            self.left.decide()
            self.right.decide()
        else:
            r1 = (self.left.decision_path, self.left.total_time)
            r2 = (self.right.decision_path, self.right.total_time)
            results.extend([r1, r2])

    def no_drink_info(self, distance):

        # Non-wait dist
        nonwait = distance - self.waiting_distance
        if nonwait < 0:
            next_wait = abs(nonwait)
            return distance, 0, self.fast_distance, next_wait
        else:
            next_wait = 0

        slow = nonwait - self.fast_distance

        if slow < 0:
            fast_left = abs(slow)
            slow = 0
        else:
            fast_left = 0
            slow = slow + self.waiting_distance

        fast = distance - slow

        return slow, fast, fast_left, next_wait

    def drink_info(self, distance):

        d1 = t*a  # Distance she walks when her coffee is getting ready
        d2 = r*b  # Distance she will walk fast

        # Non-wait dist
        nonwait = distance - d1
        if nonwait < 0:
            next_wait = abs(nonwait)
            return distance, 0, d2, next_wait
        else:
            next_wait = 0

        slow = nonwait - d2

        if slow < 0:
            fast_left = abs(slow)
            slow = 0
        else:
            fast_left = 0
            slow = slow + d1

        fast = distance - slow

        return slow, fast, fast_left, next_wait


def main():

    # Get the results
    start = Node(0, [])
    start.total_time = stands[0]/a
    global results
    results = []
    start.decide()

    # Get the best result
    best = sorted(results, reverse=False, key=lambda x: x[1])[0][0]

    total = len(best)
    idxs = [str(i) for i in range(total) if best[i]]
    print(len(idxs))
    print(" ".join(idxs))


if __name__ == "__main__":

    # Read the input --> variables are global
    l, a, b, t, r = [int(val) for val in input().split(' ')]
    n = int(input())
    stands = [int(id) for id in input().split(' ')]

    # Run the proccess
    main()
