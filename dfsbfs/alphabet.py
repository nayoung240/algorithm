
'''
BFS 풀이
bfs 지만 queue를 사용하지 않는다. set을 사용한다.
set 사용하여 시간 줄이기
'''
import sys

input = sys.stdin.readline
R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    answer =1
    dq = set([])
    dq.add((x,y,board[x][y]))
    
    while dq:
        xx,yy,visited = dq.pop()
        
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            
            if 0<=nx<R and 0<=ny<C and board[nx][ny] not in visited:
                dq.add((nx,ny,visited+board[nx][ny]))
                answer = max(answer,len(visited)+1)
                
    print(answer)
        
BFS(0,0)

'''
DFS 풀이
pypy3으로만 통과한다
백트래킹 개념 사용
'''

import sys 
from collections import deque

input=sys.stdin.readline
R,C = map(int, input().split())
arr=[list(input()) for _ in range(R)]
check=[0]*(26)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
maxi=0

def dfs(x,y,cnt):
    global maxi
    maxi = max(cnt,maxi)
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<R and ny<C and nx>=0 and ny>=0 and check[ord(arr[nx][ny])-65]==0:
            check[ord(arr[nx][ny])-65]=1
            ncnt = nt+1
            dfs(nx,ny,ncnt)
            check[ord(arr[nx][ny])-65]=0

check[ord(arr[0][0])-65]=1
dfs(0,0,1)

print(maxi)
