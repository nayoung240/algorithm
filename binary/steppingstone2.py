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
def solution2(stones, k):
    start = 1
    end = max(stones) # stone의 최대값을 max로 둔다.

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
        
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
            
    return start
