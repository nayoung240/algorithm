import sys
from collections import deque

n = int(input())
q = deque()
answer= []

for i in range(n):
  l = sys.stdin.readline().strip()
  arr = l.split(' ')
  
  if arr[0] == 'push':
    q.append(int(arr[1]))
  elif arr[0] == 'pop':
    val = q.popleft() if q else -1
    answer.append(val)
  elif arr[0] == 'size':
    answer.append(len(q))
  elif arr[0] == 'empty':
    val = 0 if q else 1
    answer.append(val)
  elif arr[0] == 'front':
    val = q[0] if q else -1
    answer.append(val)
  elif arr[0] == 'back':
    val = q[-1] if q else -1
    answer.append(val)
    
print(*answer, sep='\n')    
  
