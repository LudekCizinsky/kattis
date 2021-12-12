def main():

    # Set the input variables
    start = [int(item) for item in list(input())]
    target = [int(item) for item in list(input())]
    M = len(target)
    direction = [-1 if start[i] > target[i] else 1 for i in range(M)]
    k = int(input())
    forbidden = [[int(item) for item in list(input())] for _ in range(k)]

    # Compute the result
    count = 0
    while start != target:
        subcount = 0
        for i in range(M):
            while start[i] != target[i]:
                start[i] = start[i] + direction[i]
                if start not in forbidden:
                    subcount += 1
                else:
                    start[i] = start[i] - direction[i]
                    break

        if subcount == 0:
            return "Impossible"
        else:
            count += subcount

    return count


if __name__ == "__main__":
    print(main())
