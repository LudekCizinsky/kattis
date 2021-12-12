from itu.algs4.sorting.max_pq import MaxPQ


class Party:

    def __init__(self, votes, index):
        self.votes = votes
        self.quotient = votes
        self.n_seats = 0
        self.index = index

    def update_quotient(self):
        self.quotient = (self.votes)/(self.n_seats + 1)

    def __lt__(self, other_party):
        return self.quotient < other_party.quotient


def main():

    # Get n, m
    n, m = input().split(' ')

    # Build parties MaxPQ
    pq = MaxPQ()
    for index in range(int(n)):
        party = Party(int(input()), index)
        pq.insert(party)

    # Distribute the seats
    results = [0 for _ in range(int(n))]
    for _ in range(int(m)):
        mx_party = pq.del_max()
        mx_party.n_seats += 1
        results[mx_party.index] += 1
        mx_party.update_quotient()
        pq.insert(mx_party)

    for res in results:
        print(res)


if __name__ == "__main__":
    main()
