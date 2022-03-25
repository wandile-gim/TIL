import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")

N = int(sys.stdin.readline())
dp = []
floor = [int(sys.stdin.readline()) for _ in range(N)]

dp.append(floor[0])
dp.append(max(floor[0] + floor[1], floor[1]))
dp.append(max(floor[0] + floor[2], floor[1] + floor[2]))

for i in range(3, N):
    dp.append(max(dp[i-2] + floor[i], dp[i-3] + floor[i] + floor[i-2]))
