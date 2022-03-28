N, M = map(int, input().split())
# for i in range(min(N, M), 0, -1):
#     if N % i == 0 and M % i == 0:
#         print(i)
#         break


def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x


print(GCD(N, M))


# def LCM(x, y):
#     result = (x*y)//GCD(x, y)
#     return result


# print(LCM(10, 12))
