import sys 
sys.stdin = open("input.txt", "r")
S = list(map(str, sys.stdin.readline().lower()))
alphabet = list('abcdefghijklmnopqrstuvwxyz')
array = [-1 for _ in range(len(alphabet))]

for i in range(len(S)):
    if array[alphabet.index(S[i])] == -1 : array[alphabet.index(S[i])] = i

for i in array:
    print(i,end=' ')