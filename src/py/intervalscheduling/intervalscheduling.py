from sys import stdin
from collections import deque


def main():
  
  n = int(stdin.readline().strip())
  I = list()
  i_append = I.append

  for _ in range(n):
    s, f = [int(i) for i in stdin.readline().strip().split(" ")]
    i_append((s, f))
  
  I = sorted(I, key=lambda x: x[1])
  r = 1
  last = I[0][1]
  for i in range(1, len(I)):
    if I[i][0] >= last:
      r += 1
      last = I[i][1]
  print(r)
 
if  __name__ == "__main__":
  main()
