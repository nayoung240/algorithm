'''
permutations 순열로 풀었을 때, 정답은 맞지만 모든 케이스를 만드므로 시간초과 발생
'''
def solution(numbers):
    #1. 사전 값으로 정렬하기
    numbers_str = [str(num) for num in numbers]          
    #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers_str.sort(key=lambda num: num*3, reverse=True)       

    return str(int(''.join(numbers_str)))
