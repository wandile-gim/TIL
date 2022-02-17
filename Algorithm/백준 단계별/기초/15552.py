import sys
sys.stdin = open("input.txt", 'r')
T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]
# print(data)