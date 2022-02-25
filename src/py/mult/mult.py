from sys import stdin
from collections import deque


def main():
  
  n = int(stdin.readline().strip())
  start = None
  for _ in range(n):
    i = int(stdin.readline().strip())
    if not start:
      start = i
    elif (i % start) == 0:
      print(i)
      start = None
 
if  __name__ == "__main__":
  main()
