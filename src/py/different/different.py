import sys


for line in sys.stdin:
    line = [int(item) for item in line.split()]
    print(abs(line[0] - line[1]))
