def main():
    n, T = [int(v) for v in input().split(' ')]
    C = [int(v) for v in input().split(' ')]
    result = 0
    load = 0
    for i in range(n):
        load += C[i]
        if load > T:
            break
        else:
            result += 1
    print(result)


if __name__ == '__main__':
    main()