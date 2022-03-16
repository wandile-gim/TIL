import sys
A, B = map(str, sys.stdin.readline().split())
A = int(A[-1::-1])
B = int(B[-1::-1])
print(max(A, B))
