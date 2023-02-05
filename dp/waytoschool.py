'''
어려운 point
- 방지를 위해 왼쪽과 위로 한줄씩 더 만든다.
- 아래로, 오른쪽으로 이중 for문 돌린다.
- 점화식
'''

def solution(m, n, puddles):
    # IndexError 방지를 위해 왼쪽과 위로 한줄씩 더 만든다. [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    dp = [[0] * (m+1) for _ in range(n+1)] # dp 테이블 초기화 
    dp[1][1] = 1 # 초기값
    
    for i in range(1, n+1): # 아래로
        for j in range(1, m+1): # 오른쪽으로
            # 초기값이 변경되는것 방지
            if i == 1 and j == 1: 
                continue
            
            # 웅덩이가 존재할 경우
            if [j, i] in puddles: 
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[-1][-1] % 1000000007
        

