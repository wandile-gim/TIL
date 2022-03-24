from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    who_reported_other = defaultdict(set)  # 신고한 id 목록
    reported_by_others = defaultdict(set)  # 신고받은 id 목록

    for r in report:
        report_from, report_to = r.split(' ')  # 신고한 사람과 받은 사람 분리
        # 신고한 사람(key)에 의해 신고 받은 사람(value)
        who_reported_other[report_from].add(report_to)
        # 신고 받은 사람(key)과 신고 한 사람(value)
        reported_by_others[report_to].add(report_from)

    for id_ in id_list:
        cnt = 0
        for r_to in who_reported_other[id_]:  # _id가 신고한 목록에서 아이디를 가져옴(r_to)
            # r_to 신고한 목록의 개수가 k 이상인 경우 cnt++
            if len(reported_by_others[r_to]) >= k:
                cnt = cnt+1
        answer.append(cnt)

    return answer
