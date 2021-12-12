def main():
    N = int(input())
    result = 0
    for _ in range(N):
        P = input()
        result += int(P[:-1])**(int(P[-1]))
    print(result)

if __name__ == "__main__":
    main()