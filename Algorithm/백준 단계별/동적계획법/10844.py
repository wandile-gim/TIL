import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")

N = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

mod = 100000000
print(sum(dp[N]) % mod)
