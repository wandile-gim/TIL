import sys
sys.stdin = open("input.txt", "r")
T = int(input())
li = [list(map(str, sys.stdin.readline().split())) for _ in range(T)]

for i in range(T):
    count = 0
    temp = 0
    li[i] = list(li[i][0])    
    for j in range(len(li[i])):                
        if li[i][j] == 'O':            
            temp += 1            
        elif li[i][j] == 'X':
            temp = 0        
        count += temp        
    print(count)
    