import sys
T = int(sys.stdin.readline())

num_li = [0 for i in range(101)]

num_li[0] = 1
num_li[1] = 1
num_li[2] = 1

for i in range(3, 101):
    num_li[i] = num_li[i-3] + num_li[i-2]


for i in range(T):
    num = int(sys.stdin.readline())
    print(num_li[num-1])
