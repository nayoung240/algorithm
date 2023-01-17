'''
[10, 2, 2, 100, 2] => 110
[1, 3, 4, 3, 7] => 11
[0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1] => 201
...

통과하지 못하던 케이스
[91, 90, 5, 7, 5, 7] => 104

내림차순으로 정렬해서 더해갔는데, 맨 처음 집이 가장 크다고 최대 루트가 아니다는거에 걸림.
'''

def solution(money):
    answer = 0
    jump = []
    
    idx = [i for i in range(0, len(money))]
    moneylist = list(zip(idx, money))
    
    # 내림차순
    moneylist = sorted(moneylist, key = lambda x : x[1], reverse=True)
    
    for i,j in moneylist:
        if j == 0:
            continue
        
        if i not in jump:
            print('i',i,j)
            answer += j
            prev_i = i-1
            next_i = i+1
            
            if i == idx[-1]:
                next_i = 0
            elif i == 0:
                prev_i = idx[-1]
                
            jump.append(prev_i)
            jump.append(next_i)
        
    return answer

'''
올바른 풀이
'''

def solution(money):
    n = len(money)
    dp1 = [0] * n
    # 1번집을 터는 경우
    dp1[0] = money[0]
    dp1[1] = max(dp1[0], dp1[1]) # 2번집을 선택할 수도 있고 안할 수 도 있다.
    
    for i in range(2, n - 1): # 마지막 집은 털지 못한다
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # 1번집을 털지 않는 경우
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))
