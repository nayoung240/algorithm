'''
permutations 순열로 풀었을 때, 정답은 맞지만 모든 케이스를 만드므로 시간초과 발생

풀이포인트
sort key lambda
key인자에 함수를 넘겨주면 우선순위가 정해진다
d = sorted(a, key = lambda x : x[1]) 
d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]

'''
def solution(numbers):
    #1. 사전 값으로 정렬하기
    numbers_str = [str(num) for num in numbers]          
    #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers_str.sort(key=lambda num: num*3, reverse=True)       

    return str(int(''.join(numbers_str)))
