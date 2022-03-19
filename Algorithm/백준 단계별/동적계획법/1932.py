import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")
N = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

way = 0
for i in range(1, len(triangle)):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif i == j:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            print(i, j)
            triangle[i][j] = max(triangle[i][j] + triangle[i-1]
                                 [j], triangle[i][j] + triangle[i-1][j-1])

print(max(triangle[-1]))
