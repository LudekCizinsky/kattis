from sys import stdin
from collections import deque


def main():
  
  l, r = stdin.readline().strip().split("()")
  if len(l) == len(r):
    print("correct")
  else:
    print("fix")
   
if  __name__ == "__main__":
  main()
