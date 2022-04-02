import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(len(A))]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
# print(dp)
