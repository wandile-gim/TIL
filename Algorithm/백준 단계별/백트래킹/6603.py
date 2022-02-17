ans = []


def dfs(depth, start):
    if depth == 6:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, c):
        ans.append(li[i])
        dfs(depth+1, i+1)
        ans.pop()


while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    c = li[0]
    li = li[1:]
    dfs(0, 0)
    print()
