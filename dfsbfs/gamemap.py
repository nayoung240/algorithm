from collections import deque

def solution(maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    # -1로 그래프 생성
    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])
    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나지 않고, 벽이 아니고
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                # 처음 가는 길
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx]) # 재귀

    answer = graph[-1][-1]
    return answer
