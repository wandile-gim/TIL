import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
li = []
count = []
for _ in range(n):
    li.append(input())

for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if li[a][b] != 'W':
                        case1 += 1
                    if li[a][b] != 'B':
                        case2 += 1
                else:
                    if li[a][b] != 'B':
                        case1 += 1
                    if li[a][b] != 'W':
                        case2 += 1
        count.append(min(case1, case2))
        print(min(case1, case2))
print(min(count))
