
'''
개념1. 계산공식 : 아래부터 양옆 최대값을 더해주면서 위로 계산함
                                                                              7   -> 30
                                                         3  8   -> 23 21 -> 23 21
                              8  1  0   -> 20 13 10 -> 20 13 10
 2 7 4 4  -> 10 12 10 10 -> 10 12 10 10
4 5 2 6 5

개념2. 역순 문법
for i in range(7, -1, -1): 
    print(i)
    
# -1만큼 7 -> 6 -> 5 -> ... 0
'''

def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(0, len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1]) 
    
    return triangle[0][0]
