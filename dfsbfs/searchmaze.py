import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[-1 for _ in range(m)] for _ in range(n)]
maps = []

for _ in range(n):
  a = map(int, sys.stdin.readline().rstrip())
  maps.append(list(a))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()
queue.append([0,0])

graph[0][0] = 1

while queue:
  y, x = queue.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
      if graph[ny][nx] == -1:
        graph[ny][nx] = graph[y][x] + 1
        queue.append([ny,nx])

answer = graph[-1][-1]
print(answer)
