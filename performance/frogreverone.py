'''
처음 풀이
성능 O(N ** 2)
if False not in check: N의 복잡도가 증가한다.
'''

def solution(X, A):
    answer = -1
    check = [False] * X
    idx = 0

    if set(A) - set([i+1 for i in range(X)]):
        return answer

    for leaf in A:
        check[leaf-1] = True

        if False not in check:
            return idx

        idx += 1

    return answer

'''
두번째 풀이
성능 O(N)
'''

def solution(X, A):
    answer = -1
    check = [False] * X
    check_cnt = 0
    idx = 0

    if set(A) - set([i+1 for i in range(X)]):
        return answer

    for leaf in A:
        if check[leaf-1] == False:
            check[leaf-1] = True
            check_cnt += 1

            if check_cnt == X:
                return idx
        
        idx += 1

    return answer
