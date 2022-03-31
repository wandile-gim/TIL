import sys
path = "/Users/wonjae\
/TIL/Algorithm/백준 단계별/동적계획법/input.txt"
sys.stdin = open(path, "r")
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)] + [0]*100

dp = []
dp.append(arr[0])
dp.append(arr[0] + arr[1])
dp.append(max(arr[2]+arr[0], arr[1]+arr[2], dp[1]))

for i in range(3, N+1):
    c_1 = dp[i-1]
    c_2 = dp[i-2] + arr[i]
    c_3 = dp[i-3] + arr[i-1] + arr[i]

    dp.append(max(c_1, c_2, c_3))

print(max(dp))
# print(dp)
