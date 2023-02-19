'''
제곱근을 이용한 약수 구하기
'''

def solution(N):
    data = set()

    for i in range(1, int(N ** (1 / 2)) + 1):
        if N % i == 0:
            a = i
            b = N // i
            data.add((a + b) * 2)

    return min(data)
