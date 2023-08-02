import sys
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
checked = [0 for _ in range(N)]

print(S)

min_ans = -sys.maxsize - 1


def dfs(idx, cnt):
    global min_ans

    if N // 2 == cnt:
        pass
