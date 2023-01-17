'''
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3#_=_

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
'''

# 내 풀이는 효율성 검사에서 실패...
def fail_solution(participant, completion):
    answer = ''
            
    for cName in completion:
        
        if cName in participant:
            idx = participant.index(cName)
            del participant[idx]
            continue
    
    answer = participant[0]

    return answer

'''
해쉬 key-value 쌍 특정한 배열의 인덱스나 위치를 저장하거나 찾을 수 있다.
해시 값 자체를 index로 사용하기 때문에 평균 시간 복잡도가 O(1)로 매우 빠름.

collections.Counter
- {객체값 : counter수}
- counter 객체 간 더하기, 빼기, 교집합, 합집합 연산 가능
'''
import collections

def success_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]
