import sys
sys.stdin = open("input.txt", "r")
C = int(input())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]

def average(li):
    tot = 0
    for i in range(1, len(li)):
        tot += li[i]              
    return tot / (len(li)-1)

for i in range(len(li)):
    many = li[i][0]
    avg = average(li[i])
    over = 0
    for j in range(many+1):        
        if avg < li[i][j]:
            over += 1
    percent = (over/many)*100
    print(f'{percent:.3f}%')
