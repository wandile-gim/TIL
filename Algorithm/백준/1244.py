import sys
sys.stdin = open("백준/input.txt", "r")

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline())

for i in range(student):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        limit = N//num
        for j in range(1, limit+1):
            if switch[(num*j)-1] == 1:
                switch[(num*j)-1] = 0
            else:
                switch[(num*j)-1] = 1
    else:
        expand = 0
        j = num-1
        while True:
            j = j-1
            if switch[(num-j)-1] == switch[(num+j)-1]:
                expand = expand + 1
            if j == 0 or switch[(num-j)-1] != switch[(num+j)-1]:
                break
        if expand > 1:
            for k in range((num-expand), (num+expand)+1):
                if switch[k-1] == 1:
                    switch[k-1] = 0
                else:
                    switch[k-1] = 1
        else:
            if switch[k-1] == 1:
                switch[k-1] = 0
            else:
                switch[k-1] = 1
print(switch)
