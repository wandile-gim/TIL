n = int(input())
for i in range(1, n+1):
    candidate = list(map(int, str(i)))
    result = i + sum(candidate)
    if result == n:
        print(i)
        break

    if i == n:
        print(0)
