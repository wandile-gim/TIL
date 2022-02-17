import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(sys.stdin.readline())
li = list(set(li))
li.sort(key=lambda x: (len(x), x))
print('\n'.join(li))
