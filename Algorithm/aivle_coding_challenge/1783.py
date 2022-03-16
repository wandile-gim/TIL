N = int(input())
ans = 0
for i in range(1, N+1):
    if i % 5 == 0:
        ans = ans + 1
print(ans)
