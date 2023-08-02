import sys
sys.stdin = open("백준/input.txt", "r")

king, stone, n = sys.stdin.readline().split()
k = list(map(int, [ord(king[0])-64, king[1]]))
s = list(map(int, [ord(stone[0])-64, stone[1]]))

move = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [-1, 0],
    'T': [1, 0],
    'RT': [1, 1],
    'LT': [1, -1],
    'RB': [-1, 1],
    'LB': [-1, -1]
}

for _ in range(int(n)):
    m = input()
    dx, dy = move[m][1], move[m][0]
    nx = k[0] + dx
    ny = k[1] + dy
    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == s[0] and ny == s[1]:
            sx = s[0] + dx
            sy = s[1] + dy
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
        else:
            k = [nx, ny]
print(f"{chr(k[0] + 64)}{k[1]}")
print(f"{chr(s[0] + 64)}{s[1]}")
