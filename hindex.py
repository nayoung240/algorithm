'''
https://programmers.co.kr/learn/courses/30/lessons/42747

어떤 과학자가 발표한 논문 n편 중, 
h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 
h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''

def solution(citations):
    n = len(citations) # 발표한 논문 수
    citations.sort()

    while n >= 0:
        cnt = len([x for x in citations if x >= n])

        if cnt >= n:
            return n
        else:
            n -= 1

'''
다른 풀이
'''
def solutionOther(citations):
    n = len(citations)
    citations.sort()

    for i in range(n):
        if citations[i] >= n-i:
            return n-i

    return 0

'''
22.10.15 다시품
'''
def solution(citations):
    answer = 0
    citations_cnt = len(citations)
    
    for i in range(citations_cnt, 0, -1):
        cnt = 0
        
        for j in citations:
            if i <= j:
                cnt += 1
        
        if i <= cnt:
            answer = i
            break

    return answer
