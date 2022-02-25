from sys import stdin


def main():
  a,b = [int(n) for n in stdin.readline().split(" ")]
  if a > b:
    print(b,a)
  else:
    print(a, b)


if  __name__ == "__main__":
  main()
