def main():

  n, x, y = [int(v) for v in input().split(" ")]
  r = y / x
  for i in range(n):
    print(round(int(input())*r))


if __name__ == "__main__":
  main()
