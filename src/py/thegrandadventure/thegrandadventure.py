from sys import stdin
from collections import deque


M = {
    "t" : "|",
    "j" : "*",
    "b" : "$"
}

def main():
  
  n = int(stdin.readline().strip())

  for _ in range(n):

    a = deque(stdin.readline().strip())
    bag = deque()
    fail = False

    while a:
      try:
        i = a.popleft()
        if i in ["$", "|", "*"]:
          bag.appendleft(i)
        elif i in ["t", "b", "j"]:
          o1 = M[i]
          o2 = bag.popleft()
          if o1 != o2:
            fail = True
            break 
      except Exception as e:
        fail = True
        break

    if len(bag) > 0 or fail:
      print("NO")
    else:
      print("YES")
           
if  __name__ == "__main__":
  main()
