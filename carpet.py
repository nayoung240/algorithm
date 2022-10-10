'''
https://programmers.co.kr/learn/courses/30/lessons/42842

Leo가 본 카펫에서 갈색 격자의 수 brown, 
노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''
def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    i = 3

    while True:
        if total % i == 0:
            j = total / i

            if (i - 2) * (j - 2) in [brown, yellow]:
                break
        
        i += 1

    answer = [i, j]

    return answer

'''
22.10.10 다시 풀었다.

풀이 포인트
1. 최소길이는 3개가된다.
2. 갈색 = x*y / 노란색 = (x-2)*(y-2)
3. 길이들을 for문을 돌면서 조건이 만족할 때까지 완전탐색
'''
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(3,total+1):
        if total % h == 0:
            w = total/h
            if (w - 2) * (h - 2) == yellow:
                answer = [w,h]
                break
                
    return answer
