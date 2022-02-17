import sys
sys.stdin = open("input.txt", "r")
a,b = map(str,sys.stdin.readline().split())
a,b = a[-1::-1], b[-1::-1]
a, b = int(a), int(b)
print(max(a,b))
