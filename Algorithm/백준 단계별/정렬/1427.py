import sys
sys.stdin = open("input.txt", "r")

li = list(map(int, sys.stdin.readline()))
li.sort(reverse=True)
for i in range(len(li)):
    print(li[i], end='')
