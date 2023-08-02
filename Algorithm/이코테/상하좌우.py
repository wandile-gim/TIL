n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

direction = ['L', 'R', 'U', 'D']
x, y = 1, 1
for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
