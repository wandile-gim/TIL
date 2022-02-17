from glob import glob


li = []
n, m = 4, 2


# def nm49():
#     if len(li) == m:
#         print(' '.join(list(map(str, li))))
#         return
#     for i in range(1, n + 1):
#         if i not in li:
#             li.append(i)
#             nm49()
#             li.pop()


# nm49()


def nm50(start):
    if len(li) == m:
        print(li)
        return
    for i in range(start, n + 1):
        li.append(i)
        nm50(i+1)
        li.pop()


# nm50(1)

def nm51():
    if len(li) == m:
        print(li)
        return
    for i in range(1, n+1):
        li.append(i)
        nm51()
        li.pop()


# nm51()

def nm52(start):
    if len(li) == m:
        print(li)
        return
    for i in range(start, n+1):
        li.append(i)
        nm52(i)
        li.pop()


# nm52(1)

a = 0


def d():
    global a
    a += 1
    return a + 3


print(d())
