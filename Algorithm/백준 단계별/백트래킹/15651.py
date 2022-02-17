n, m = map(int, input().split())

li = []


def dfs():
    if len(li) == m:
        print(' '.join(list(map(str, li))))
        return
    for i in range(1, n+1):
        li.append(i)
        dfs()
        li.pop()


dfs()
