N = int(input())

cnt = 0
for i in range(2, N+1):
    flag = 0
    for j in range(2, int((i**0.5))+1):
        if i % j == 0:
            flag += 1
            break
    if flag == 0:
        cnt = cnt+1
print(cnt)
