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

if citations[i] >= article_count-i는 주어진 h번 이상 인용된 논문이 h편 이상이라는 조건을 그대로 풀어쓴 것이었다.
citations[i]는 i번 논문이 인용된 횟수이고 article_count-i는 인용된 논문의 개수를 최댓값부터 하나씩 줄여나간 것이다. (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
그리고 리스트는 오름차순 정렬된 상태이므로 i번째 이후는 모두 i번째보다 큰 값을 가질 것이다.
'''
def solutionOther(citations):
    article_count = len(citations)
    citations.sort()

    for i in range(article_count):
        if citations[i] >= article_count-i:
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
