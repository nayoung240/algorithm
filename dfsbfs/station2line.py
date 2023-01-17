'''
참고 https://data-flower.tistory.com/105
푸는 방법이 다양하지만. dfs와 bfs를 이용해서 푸는 풀이법
어려움

필요개념
- 순환그래프 (dfs)
'''

import sys
from collections import deque
sys.setrecursionlimit(10**9) # 재귀호출 시 필수
input = sys.stdin.readline

def dfs(x, cnt):
    global idx
    # 시작역과 현재역이 일치할 때 && 두번이상 다른역 방문할 때 순환역
    if x == idx and cnt >= 2:
        isCycle[idx] = 1
        return
  
    visited[x] = 1
    for j in graph[x]:
        # 아직 방문하지 않은 역이라면
        if not visited[j]:
            dfs(j, cnt + 1)
        # 이미 방문하고, 2곳 이상 방문했다면
        elif j == idx and cnt >= 2:
            dfs(j, cnt)


def bfs():
    q = deque()
    for i in range(1, N+1):
        if isCycle[i]:
            q.append(i)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not dis[i]:
                if not isCycle[i]:
                    dis[i] = dis[x] + 1
                    q.append(i)


N = int(input())
graph = [[] for _ in range(N+1)]
isCycle = [0] * (N+1)
dis = [0] * (N+1)

for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 순환역에 해당하는 역 표시 dfs
for idx in range(1, N+1):
    visited = [0] * (N+1)
    dfs(idx, 0)

# 각 역과 순환선 사이의 최소 거리 구하기 bfs
bfs()

print(*dis[1:])
