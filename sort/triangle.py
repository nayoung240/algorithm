'''
내 풀이
시간복잡도: O(N*log(N))
'''

from collections import deque
def solution(A):
    answer = 0
    count = 0
    A.sort(reverse=True)
    A = deque(A)

    while count < len(A)-2:
        max_num = A.popleft()
        count += 1

        if A[0] + A[1] > max_num and A[0] + max_num > A[1] and A[1] + max_num > A[0]:
            answer = 1
            break

    return answer
  
'''
다른 풀이를 보니 굳이 deque를 안해도 ...

a < b < c이렇게 정렬이 될때,
일단 a + c > b 는 당연한 사실 c가 b 보다 크기 때문에.
그리고 c + b > a도 당연한 사실 c,b가 a보다 크기 때문에,
그러므로 a + b > c 인지만 확인하면 됨.

시간복잡도: O(N*log(N))
'''
def solution(A):
    A = sorted(A)
    
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    
    return 0  
