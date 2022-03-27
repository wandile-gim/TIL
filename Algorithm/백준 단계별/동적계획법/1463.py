import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")

X = int(sys.stdin.readline())

dp = [0 for i in range(X+1)]

for i in range(2, X+1):
    dp[i] = dp[i-1]+1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[X])

# import sys
# read = sys.stdin.readline

# N = int(read())
# cache = {1: 0, 2: 1}

# def dp(n):
#     if n in cache:
#         return cache[n]

#     # 핵심 코드
#     cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
#     cache[n] = cnt
#     return cnt

# print(dp(N))
