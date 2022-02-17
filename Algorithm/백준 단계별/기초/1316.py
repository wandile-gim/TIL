from os import rename
import sys
sys.stdin = open("input.txt", "r")
N = int(input())
cnt = 0
for i in range(N):
    line = sys.stdin.readline();
    for j in range(len(line)-1):
        if line[j] == line[j+1]:
            continue
        elif line[j] in line[j+1:]:
            cnt += 1
            break
print(N-cnt)