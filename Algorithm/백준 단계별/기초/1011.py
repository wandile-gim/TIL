import sys
sys.stdin = open("input.txt", "r")
T = int(sys.stdin.readline())
k = 0
a, b, c = k-1, k, k+1
for i in range(T):
    operation = 0
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y+1):
        if a == -1:
            b = 1
        if y - x <= 1:
            x += 1
            operation += 1
        if c < y:
            k = k+1
            x = x + k
            operation += 1
    print(operation)