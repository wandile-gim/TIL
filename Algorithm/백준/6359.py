import sys
sys.stdin = open("백준/input.txt", "r")

# 열림 1
# 닫힘 0


def solution(n):
    li = [1]*n
    for i in range(2, n+1):
        limit = n//i
        for j in range(1, limit+1):
            if i == 2:
                li[(i*j)-1] = 0
            else:
                if li[(i*j)-1] == 0:
                    li[(i*j)-1] = 1
                else:
                    li[(i*j)-1] = 0
    return li.count(1)


T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    print(solution(n))
