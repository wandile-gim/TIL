n, m = map(int, input().split())
map_history = [[0 for i in range(n)] for j in range(m)]
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for j in range(m)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map_history[x][y] = 1


def turn_left():
    global d
    d = - 1
    if d == -1:
        d = 3


count = 1
turned = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if map_history[nx][ny] == 0 and map[nx][ny] == 0:
        map_history[nx][ny] = 1
        x = nx
        y = ny
        turned += 1
        count += 1
        continue
    else:
        turned += 1

    if turned == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turned = 0
print(count)
