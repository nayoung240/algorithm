'''
circle 0 to N - 1
if you ate chocolate number X, 
then you will next eat the chocolate with number (X + M) modulo N

0 1 2 3 4 5 6 7 8 9

0 0+4 4+4 4+4+4 4+4+4+4

유클리드 알고리즘 - 최대공약수 구하기
'''
def solution(N, M):
    from math import gcd
    return N//gcd(M,N)
