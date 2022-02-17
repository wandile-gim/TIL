from collections import Counter
import sys

from numpy import sort
sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for i in range(N)]


def average(li):
    return round(sum(li) / len(li))


def middle(li):
    li = sorted(li)
    index = len(li) // 2
    return li[index]


def most(li):
    max_value = 0
    return_li = []
    for i in li:
        if max_value == li.count(i):
            return_li.append(i)
        elif max_value < li.count(i):
            return_li = []
            return_li.append(i)
            max_value = li.count(i)
    if len(return_li) > 1:
        return_li.sort()
        return return_li[1]
    else:
        return return_li[0]
# def most(li):
#     li = sorted(li)
#     c = Counter(li).most_common()
#     if len(li) > 1:
#         if c[0][1] == c[1][1]:
#             return c[1][0]
#         else:
#             return c[0][0]
#     else:
#         return c[0][0]


print(average(li))
print(middle(li))
print(most(li))
new_li = sorted(li)
print(new_li[-1] - new_li[0])
