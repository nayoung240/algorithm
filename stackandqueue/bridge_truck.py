'''
틀렸던 부분
트럭이 지나가는데 bridge_length 만큼 시간만큼 소요되는 점을 놓쳤다. 1초만에 완료되는 줄 알았다.
근데 알았는데도 구현에 실패했다.
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0 #다리위 트럭 무게 합
    truck_bridge_deque = deque(bridge_length * [0]) #다리 단위 만큼
    truck_weights_deque = deque(truck_weights)
    
    while len(truck_bridge_deque):
        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()
        
        if truck_weights_deque:
            # 다리위에 트럭이 더 올라갈 수 있으면
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)
    return answer
