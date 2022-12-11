from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_bridge_dq = deque(bridge_length * [0]) # 다리 단위 만큼
    truck_weights_dq = deque(truck_weights)
    
    while len(truck_bridge_dq):
        print(truck_bridge_dq)
        answer += 1
        truck_bridge_dq.popleft()
        
        if truck_weights_dq:
            # 다리위에 더 트럭 추가 가능할 경우
            if sum(truck_bridge_dq) + truck_weights_dq[0] <= weight:
                truck_bridge_dq.append(truck_weights_dq.popleft())
            else:
                truck_bridge_dq.append(0)
    return answer
