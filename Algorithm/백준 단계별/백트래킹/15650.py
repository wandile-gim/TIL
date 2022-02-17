li = []
n, m = 4, 2


def nm50(start):
    if len(li) == m:
        print(li)
        return
    for i in range(start, n + 1):
        li.append(i)
        nm50(i+1)
        li.pop()


# nm50(1)
