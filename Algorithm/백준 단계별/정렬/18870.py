import sys
sys.stdin = open("input.txt", "r")

n = sys.stdin.readline()
li = list(map(int, sys.stdin.readline().split()))
set_li = sorted(list(set(li)))

dic = {set_li[i]: i for i in range(len(set_li))}
for i in li:
    print(dic[i], end=' ')
# list.index(i) -> O(n)의 시간 복잡도
# index[]인덱싱 O(1)의 시간 복잡도
