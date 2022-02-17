import sys
sys.stdin = open("input.txt","r")
# T = sys.stdin.readline().upper()
# alpha = list('abcdefghijklmnopqrstuvwxyz'.upper())
# arr = [0] * 26
# for i in T:
#     arr[(ord(i)-1)%ord('Z')-64]+=1

# if arr.count(max(arr)) > 1:
#     print('?')
# else:
#     maxIndex = max(arr);
#     print(alpha[arr.index(maxIndex)])
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])