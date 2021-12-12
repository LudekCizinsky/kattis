class Chessboard:

    def __init__(self, N):
        self.N = N
        self.visited = set()

    def in_range(self, i, j):
        in_range_row = 0 <= i and i < self.N
        in_range_col = 0 <= j and j < self.N
        return in_range_row and in_range_col
    
    def vis(self, i, j):
        return (i, j,) in self.visited
    
    def left_up(self, i, j):
        row, col = i - 1, j - 1
        if self.in_range(row, col):
            self.visited.add((row, col,))
            self.left_up(row, col)

    def right_up(self, i, j):
        row, col = i - 1, j + 1
        if self.in_range(row, col):
            self.visited.add((row, col,))
            self.right_up(row, col)
    
    def left_down(self, i, j):
        row, col = i + 1, j - 1
        if self.in_range(row, col):
            self.visited.add((row, col,))
            self.left_down(row, col)
    
    def right_down(self, i, j):
        row, col = i + 1, j + 1
        if self.in_range(row, col):
            self.visited.add((row, col,))
            self.right_down(row, col)
    
    def explore(self, i, j):
        if not self.vis(i, j):
            self.visited.add((i, j))
            self.left_up(i, j)
            self.right_up(i, j)
            self.left_down(i, j)
            self.right_down(i, j)
            return 1
        else:
            return 0

def main():
    
    N = int(input())
    while N:
        result = 0
        ch = Chessboard(N)
        for i in range(N):
            for j in range(N):
                add = ch.explore(i, j)
                result += add
        print(result)
        try:
            N = int(input())
        except Exception as e:
            return


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10**6)
    main()