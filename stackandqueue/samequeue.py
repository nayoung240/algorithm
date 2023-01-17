'''
문제 포인트
1. 최대 큐길이*3번 만큼만 반복한다.
2. while문 안에서 sum을 하게되면 시간 초과가 발생한다.
'''
from collections import deque 

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    q1sum = sum(q1)
    q2sum = sum(q2)
    cnt = 0
    max_cnt = len(q1) * 3

    while max_cnt != cnt:
        # 합이 더 큰 queue에서 popleft
        if q1sum > q2sum:
            q1pop = q1.popleft()
            q2.append(q1pop)
            q1sum -= q1pop
            q2sum += q1pop
        elif q1sum < q2sum:
            q2pop = q2.popleft()
            q1.append(q2pop)
            q1sum += q2pop
            q2sum -= q2pop
        else:
            return cnt

        cnt += 1

    return -1
