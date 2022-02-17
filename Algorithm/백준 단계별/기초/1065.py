import sys

# N = int(input())
N = 110
hansu = 0
for i in range(1,N+1):
    if i < 100:
        hansu += 1
    else:
        li = list(map(int, str(i)))
        if li[1] - li[0] == li[2] - li[1]:
            hansu += 1
print(hansu)