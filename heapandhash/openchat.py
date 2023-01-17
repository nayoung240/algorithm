'''
코딩테스트 연습 >2019 KAKAO BLIND RECRUITMENT>오픈채팅방
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 
최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
'''

def solution(record):
    answer = []
    uinfo = {}
    msg = []
    trans = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}

    for i in record:
        tmp = i.split(" ") 
        action = tmp[0]
        uid = tmp[1]

        if action != "Leave":
            unick = tmp[2]
            uinfo[uid] = unick            

        if action != "Change":
            msg.append([uid, action])

    for i in msg:
        answer.append(uinfo[i[0]]+trans[i[1]])

    return answer
