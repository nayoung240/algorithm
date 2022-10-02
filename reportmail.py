'''
id_list: 이용자 ID
report: 각 이용자가 신고한 ID ex) ['A B','B C'] 
k: 정지 기준이 되는 신고 횟수
return 각 유저별로 처리결과 메일받은 수

교집합: list(set(A) & set(B))
합집합: list(set(A) | set(B))
차집합: list(set(A) - set(B))
'''
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_history = defaultdict(list)
    report_cnt = defaultdict(int)

    for rep in report:
        reparr = rep.split(' ')

        # 같은 유저가 동일한 유저 신고한 경우는 제외
        if reparr[1] not in report_history[reparr[0]]:
            report_history[reparr[0]].append(reparr[1])
            report_cnt[reparr[1]] += 1

    stop_id = [i for i in report_cnt if report_cnt[i] >= k]

    for id in id_list:
        # 신고했던 유저와 이용 정지 유저와 교집합
        mail = list(set(list(report_history[id])) & set(stop_id))
        answer.append(len(mail))

    return answer
