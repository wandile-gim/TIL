from itertools import count
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

li = [list(map(int, input().split())) for i in range(n)]
ans = []
for x in li:
    count = 1
    for i in range(len(li)):
        if x[0] < li[i][0] and x[1] < li[i][1]:
            count += 1
    ans.append(count)
print(' '.join([str(i) for i in ans]))
