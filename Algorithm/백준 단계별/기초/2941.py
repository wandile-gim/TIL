import sys
sys.stdin = open("input.txt","r")
line = sys.stdin.readline()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro:
    if line.__contains__(i):
        line = line.replace(i,"*")
print(len(line))