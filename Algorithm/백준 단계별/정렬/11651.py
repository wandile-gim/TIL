import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

li.sort(key=lambda x: (x[1], x[0]))
for i in li:
    print(i[0], i[1])
