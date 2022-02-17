n = int(input())
chess = [0] * n
ans = 0


def check_valid(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
            return False

    return True


def dfs(idx):
    global ans

    if idx == n:
        ans += 1
        return

    for i in range(n):
        chess[idx] = i
        if check_valid(idx):
            dfs(idx+1)


dfs(0)
print(ans)
