from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)

    while dq:
        price = dq.popleft()
        count = 0

        for x in dq:
            count += 1

            if price > x:
                break

        answer.append(count)

    return answer
