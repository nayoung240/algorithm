'''
stones 디딤돌에 적힌 숫자 배열 (최대 크기 2십만, 최대 숫자 2억)
k 한번에 건널 수 있는 디딤돌 최대 칸수
return 최대 몇명 건널 수 있는지

그냥 while문 + for문 했을 때는 시간 초과 발생 !
'''
def solution(stones, k):
    answer = 0
    isPass = True
    
    while True:
        jump = 1
        
        for i in range(len(stones)):
            if stones[i] > 0:
                # 건너뛸 수 있는 거리 초과하면
                if k < jump:
                    isPass = False
                    break
                else:
                    jump = 1
                    
                stones[i] -= 1
            else:
                jump += 1
        
        if isPass == False:
            break
            
        answer += 1
        
    return answer


'''
=> 이분탐색 => But 뭐를 기준으로 이분탐색해야할까?
'''
def solution(stones, k):
    left = 1
    right = max(stones)
    res = 1
    
    while left <= right:
        mid = (left + right) // 2  # 건너는 친구 수 
        cnt = 0  

        # mid명 건넌다고 가정했을 때 연속 점프수 -> k 초과 시 건너기 불가능하다고 판단하고 break
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                
                if cnt >= k:
                    right = mid - 1  # 건널 수 없음 -> 건널 사람 줄이기
                    break
            else:
                cnt = 0        
        else:  # break없이 loop 무사 탈출 -> mid명 건널 수 있음 -> 건널 사람 늘리기
            res = mid
            left = mid + 1

    return res
