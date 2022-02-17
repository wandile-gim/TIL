import sys
sys.stdin = open("input.txt", "r")
a,b,c = map(int,sys.stdin.readline().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))

    