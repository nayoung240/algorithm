'''
x 바다
숫자 무인도
return 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순

bfs recursive 를 사용한다.
'''
import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    rows = len(maps)
    cols = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    #recursive bfs
    def bfs(r,c) :
        visited[r][c] = True
        area = 0
        for i in range(4):
            r1,c1 = r + dx[i], c + dy[i]
            if 0 <= r1 < rows and 0 <= c1 < cols and maps[r1][c1] != 'X' and not visited[r1][c1]:
                area += bfs(r1,c1) 
        return int(maps[r][c]) + area

    #start search
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == False and maps[i][j] != 'X':
                answer.append(bfs(i,j))

    if answer:
        answer.sort()
    else:
        answer = [-1]
        
    return sorted(answer)
