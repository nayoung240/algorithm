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
