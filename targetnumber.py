'''
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

numbers	        target	return
[1, 1, 1, 1, 1]	3	    5
[4, 1, 2, 1]	4	    2
'''
count = 0

def dfs(idx, value, numbers, target):
    global count #전역변수 count 사용 선언
    length = len(numbers)
    
    # 재귀함수 base case
    # 문제가 충분히 작아서 바로 풀수 있는 경우
    # return으로 함수 종료를 해줘야함
    if idx == length:
        if value == target:
            count+= 1
        return 
    
    # 재귀함수 recursive case
    # 재귀적으로 부분 문제를 푸는 경우.
    dfs(idx+1, value + numbers[idx], numbers, target)
    dfs(idx+1, value - numbers[idx], numbers, target)

def solution(numbers, target):
    global count
    dfs(0,0, numbers, target)
    return count

'''
22.10.11 풀이
1. 수행동작을 먼저 구현한다
2. 탈출조건을 구현한다
3. 재귀함수를 자세하게 그려보기
'''
answer = 0
tnum = 0

def solution(numbers, target):
    global tnum, answer 
    tnum = target 
    dfs(numbers, 0, 0)
     
    return answer
    
def dfs(numbers, idx, numsum):
    global tnum, answer

    # 탈출조건
    if idx == len(numbers):
        if numsum == tnum:
            answer += 1
        return
    
    # 수행동작
    dfs(numbers, idx+1, numsum+numbers[idx])
    dfs(numbers, idx+1, numsum-numbers[idx])
    
    
    
