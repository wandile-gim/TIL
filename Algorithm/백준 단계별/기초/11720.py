import sys 
sys.stdin = open("input.txt", "r")

N = sys.stdin.readline()
line = sys.stdin.readline()
ans1 = sum(list(map(int,line.strip())))
print(ans1)
