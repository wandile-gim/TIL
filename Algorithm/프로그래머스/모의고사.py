def solution(answers):
    answer = []
    way1 = [1, 2, 3, 4, 5]
    way2 = [2, 1, 2, 3, 2, 4, 2, 5]
    way3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(len(answers)):
        if way1[i % 5] == answers[i]:
            cnt1 = cnt1+1
        if way2[i % 8] == answers[i]:
            cnt2 = cnt2+1
        if way3[i % 10] == answers[i]:
            cnt3 = cnt3+1
    cnt = [cnt1, cnt2, cnt3]
    max_cnt = max(cnt)

    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            answer.append(i+1)
    return answer
