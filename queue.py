'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

sys.stdin.readline().strip(): 개행문자까지 입력받기
print(*answer, sep='\n'): 리스트 요소들 사이에 sep 구분자를 넣어 출력하기  
'''
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
 
