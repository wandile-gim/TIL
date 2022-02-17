n, m = map(int, input().split())
arr = [0] * m
visited = [0] * (n+1)


# def dfs(depth):
#     if depth == m:
#         print(*arr)
#         return
#     for i in range(1, n+1):
#         if not visited[i]:
#             visited[i] = 1
#             arr[depth] = i
#             dfs(depth+1)
#             visited[i] = 0


# dfs(0)

def dfs(depth, seq):
    if depth == m:
        print(' '.join(list(map(str, seq))))
        return
    for i in range(1, n+1):
        if i not in seq:
            temp = seq.copy()
            temp.append(i)
            dfs(depth+1, temp)


li = []


# def dfs(start):
#     if len(li) == m:
#         print(' '.join(list(map(str, li))))
#         return
#     for i in range(start, n+1):
#         if i not in li:
#             li.append(i)
#             dfs(i+1)
#             li.pop()


dfs(0, [])
