import sys
sys.stdin = open("input.txt","r")
T = int(sys.stdin.readline());

for i in range(T):
    num, alpha = sys.stdin.readline().split()
    for j in range(len(alpha)):
        for k in range(int(num)):
            print(alpha[j], end= '')
    print()        
