from itertools import permutations

# 소수 체크
def checkPrime(n):
    if n < 2:                                 
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니다
    
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    temp = []
    
    # 조합찾기
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i)) 
    
    num = [int(''.join(t)) for t in temp] 
    
    for i in num:
        if checkPrime(i):
            answer.append(i)
    
    return len(set(answer))

  
 '''
 에라토스테네스의 체 
 - 제곱근 이용
 '''

from itertools import permutations

def solution(n):
    a = set()
    
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        
    a -= set(range(0, 2))
    
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
        
    return len(a)

    
