import sys
sys.stdin = open("input.txt","r")
S = sys.stdin.readline()
# alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
# dic = {}
# cost = 0
# for i in range(8):
#     if i == 5:
#         dic[i+3] = alphabet[i*3 : i*3+4]
#     elif i == 6:
#         dic[i+3] = alphabet[i*3+1 : i*3+4]
#     elif i == 7:
#         dic[i+3] = alphabet[i*3+1:]
#     else:
#         dic[i+3] = alphabet[i*3: i*3+3]

# for i in S:
#     for k, v in dic.items():
#         li = list(v)
#         if li.count(i) >= 1:
#             cost += k
# print(cost)
numbers = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cost = 0 
for i in S:
    for number in numbers:
        if i in number:
            cost += numbers.index(number) + 3
print(cost)