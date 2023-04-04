import sys
sys.setrecursionlimit(10000)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
count = 0

for i in range(e): 
  v1, v2 = map(int, sys.stdin.readline().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, v+1):
  if not visited[i]:
    dfs(i)
    count += 1
