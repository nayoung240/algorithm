'''
1차 풀이 (실패)
성능: O(N**2)
'''
def solution(A):
    arr = set(A)

    for n in arr:
        cnt = A.count(n)
        if cnt % 2 != 0:
            return n
'''
2차 풀이 (성공)
성능: O(N) or O(N*log(N))
'''
import collections

def solution(A):
    countA = collections.Counter(A)

    for v in countA:
        if countA[v] % 2 != 0:
            return v
