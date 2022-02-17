import sys

sys.stdin = open("input.txt", "r")
N = int(input())
v = list(map(int, sys.stdin.readline().split()))
tot = 0
maxPoint = max(v)
for i in range(N):
    v[i] = (v[i] / maxPoint) * 100
    tot += v[i]
print(tot/N)

