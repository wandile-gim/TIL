A = int(input())


def ans(A):
    if A >= 90:
        print("A")
        return
    if A >= 80 and A < 90:
        print("B")
        return
    if A < 80 and A >= 70:
        print("C")
        return
    print("F")


ans(A)
