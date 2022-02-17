import sys
sys.stdin = open("input.txt","r")
S = input()
print(len(list(S.lstrip().rstrip().split())))