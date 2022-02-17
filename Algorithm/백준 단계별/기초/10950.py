import sys
sys.stdin = open("input.txt", 'r')
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    print(a+b)