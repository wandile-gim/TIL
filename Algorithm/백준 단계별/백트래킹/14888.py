import sys

N = int(input())
A = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

max_ans, min_ans = -sys.maxsize - 1, sys.maxsize


def dfs(num, idx, plus, minus, multi, div):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return

    if plus > 0:
        dfs(num + A[idx], idx + 1, plus-1, minus, multi, div)
    if minus > 0:
        dfs(num - A[idx], idx + 1, plus, minus-1, multi, div)
    if multi > 0:
        dfs(num * A[idx], idx + 1, plus, minus, multi-1, div)
    if div > 0:
        dfs(int(num / A[idx]), idx + 1, plus, minus, multi, div-1)


dfs(A[0], 1, plus, minus, multi, div)
print(max_ans)
print(min_ans)
