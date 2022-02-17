import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
li = [list(sys.stdin.readline().split()) for i in range(n)]
li.sort(key=lambda x: (int(x[0])))
for i in li:
    print(' '.join(i))
