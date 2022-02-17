import sys
# sys.stdin = open("input.txt", "r")
n = int(input())

i = 0
ragnarok = '666'
increase = 666
while True:
    if ragnarok in str(increase):
        i += 1

    if i == n:
        print(increase)
        break
    increase += 1
