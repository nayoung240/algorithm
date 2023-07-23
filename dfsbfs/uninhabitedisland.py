'''
x 바다
숫자 무인도
return 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순

<누군가의 정답>
bfs recursive 를 사용한다.
bfs()를 선언
bfs()는 재귀적으로 호출되며, 특정 지점에서 네 방향을 탐색하고 방문처리
유효한 탐색 방향에 대해 다시 bfs() 수행 후 결과들을 합산
bfs를 시작한 지점에서의 결과와 다시 합산하여 return
방문하지 않은 지점을 우선으로 전부 탐색하여 결과를 리스트에 저장
리스트를 정렬. 리스트가 비어있으면 [-1]
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
            r1 = r + dx[i]
            c1 = c + dy[i]
            
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
