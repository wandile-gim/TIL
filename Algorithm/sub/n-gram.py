s = ['xddxdca', 'jpcpjppcyycyy', 'brbabrrara', 'xxx', 'gwgwgw']


def solution(s):
    answer = []
    dic = {}
    for alphabet in s:
        dic[alphabet] = s.count(alphabet)
    dic = sorted(dic.items(), key=lambda target: target[1], reverse=True)
    max_value = dic[0][1]
    second = 0
    for i in range(len(dic)):
        if dic[i][1] == max_value:
            second = second + 1

    if len(dic) > second:
        second_value = dic[second][1]
    else:
        second_value = dic[second-1][1]

    for i in range(len(dic)):
        if dic[i][1] == second_value:
            if len(dic) > second+1:
                answer.append(dic[i][0])
            else:
                answer.append("-")

    answer = sorted(answer)
    return ''.join(set(answer))
    # 두 번째로 큰 인덱스의 위치와 같은


for i in range(len(s)):
    print(solution(s[i]))
