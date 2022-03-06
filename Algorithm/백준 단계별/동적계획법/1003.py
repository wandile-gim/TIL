T = int(input())

one = [1, 0, 1]
zero = [0, 1, 1]


def ans(num: int):
    length = len(one)
    for n in range(length, num+1):
        zero.append(zero[n-2]+zero[n-1])
        one.append(one[n-2]+one[n-1])
    print(one[num], zero[num])


for i in range(T):
    num = int(input())
    ans(num)
