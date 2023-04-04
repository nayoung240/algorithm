# algorithm 문제 모음

## 스택/큐

<details><summary><b>👀문제풀이</b></summary>

* 스택 수열 ▪▪
[문제](https://www.acmicpc.net/problem/1874) ▪▪ [풀이](/stackandqueue/stacknumber.py)
* 1~1000에서 각 숫자의 개수 구하기 ▪▪
[문제](https://codingdojang.com/scode/504) ▪▪ [풀이](/stackandqueue/numbercount.py)
* 큐2 ▪▪
[문제](https://www.acmicpc.net/problem/18258) ▪▪ [풀이](/stackandqueue/queue.py)

<img src="https://img.shields.io/badge/programmers-blue"/>

* 스택/큐 > 기능개발 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/42586) ▪▪ [풀이](/stackandqueue/functiondevlop.py)
* 스택/큐 > 주식 가격 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42584) ▪▪ [풀이](/stackandqueue/stockprice.py)
* 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/64061?language=javascript) ▪▪ [풀이](/stackandqueue/dolldraw.js)
* 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/118667) ▪▪ [풀이](/stackandqueue/samequeue.py)
* 스택/큐 > 다리를 지나는 트럭 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42583) ▪▪ [풀이](/stackandqueue/bridge_truck.py)

<img src="https://img.shields.io/badge/codility-orange"/>

* Brackets ▪▪
[문제](https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/start/) ▪▪ [풀이](/stackandqueue/brackets.py)
* Fish ▪▪
[문제](https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/start/) ▪▪ [풀이](/stackandqueue/fish.py)
* StoneWall ▪▪
[문제](https://app.codility.com/c/run/trainingB2Q6QP-WRP/) ▪▪ [풀이](/stackandqueue/stonewall.py)

</details><br>


## 힙/해시

### ✨해시맵

- 메모리를 사용하여 시간복잡도를 줄인다.
- 배열 내 빈도수 구하기
- 배열 내 중복된 요소 구하기

### ✨힙 heap
: 여러개의 값들 중에서 최대값이나 최솟값을 빠르게 찾도록 만들어진 자료구조

- 이진 트리 구조
- 각 노드의 값은 자식 노드보다 크거나 같다. (이진탐색 트리와의 차이점)
- 두 자식 중 더 큰 자식과 자신의 위치를 바꾸는 알고리즘
- 최악은 O(logN)

### 최소힙 (오름차순 정렬)
: 부모노드의 값이 자식노드의 값보다 항상 작다.
```
import heapq

def heapsort(iterable):
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

### 최대힙 (내림차순 정렬)
: 부모노드의 값이 자식노드의 값보다 항상 크다.
```
import heapq

def heapsort(iterable):
    r = []
    result = []

    for value in iterable:
        heapq.heappush(r,-value)
    
    for _ in range(len(r)):
        result.append(-heapq.heappop(r))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/leetcode-green"/>

* Kth Largest Element in an Array ▪▪
[문제](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) ▪▪ [풀이](/heapandhash/kthlagest.py)
* Kth Smallest Element in a Sorted Matrix ▪▪
[문제](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/) ▪▪ [풀이](/heapandhash/kthsmallest.py)
* Group Anagrams ▪▪
[문제](https://leetcode.com/problems/group-anagrams/description/) ▪▪ [풀이](/heapandhash/groupanagram.py)
* Letter Combinations of a Phone Number ▪▪
[문제](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)  ▪▪ [풀이](/heapandhash/phonenumbercombination.py)
* Determine if Two Strings Are Close ▪▪
[문제](https://leetcode.com/problems/determine-if-two-strings-are-close/description/)  ▪▪ [풀이](/heapandhash/closestring.py)

    
<img src="https://img.shields.io/badge/programmers-blue"/>

* 해시 > 완주하지 못한 선수 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3#_=_) ▪▪ [풀이](/heapandhash/uncomplete.py)
* 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42888) ▪▪ [풀이](/heapandhash/openchat.py)
* 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/92334) ▪▪ [풀이](/heapandhash/reportmail.py)

</details><br>

## 정렬
- sort(): 리스트 원본값을 수정한다, 리턴값은 None (sorted 보다 조금 빠르다)
- sorted(): 리스트 원본값은 그대로, 리턴값은 정렬값

### 중복제거&정렬하기
```
sorted(set(nums), reverse=True)
```

### lamda 인자 : 표현식 
- key인자에 정렬해줄 값을 넘겨주면 정렬된다 

### list[1]을 기준으로 정렬
```
sorted(a, key = lambda x : x[1]) # [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]
```
### 문자열 길이를 기준으로 정렬
```
sorted(list, key=lambda x : len(x)) # ['is', 'my', 'name', 'song']
```
### 제일 큰 수 만들기
```
list.sort(key=lambda x:str(x)*3, reverse=True)
```

### ✨정렬 알고리즘
1. Bubble Sort(버블정렬): 첫 원소부터 순차로 현재 원소가 그 다음 원소보다 크면 두 원소를 바꿈
2. Selection Sort(선택정렬): 배열을 선형 탐색(linear scan)하여 가장 작은 원소를 앞으로 보냄
3. Insertion Sort(삽입정렬): 적절한 위치에 삽입(insertion)하는 정렬. 필요할 때만 위치를 바꾸므로 데이터가 정렬되어있을 때는 효율적임.
4. Quick Sort(퀵정렬): 임의의 기준 대비 큰 수와 작은 수로 나누는 방식
5. Merge Sort(병합정렬): 배열을 절반씩 나누어 각각 정렬하고 합해서 다시 정렬
6. Heap Sort(힙정렬): 루트를 힙의 마지막 원소와 교환하고, 나머지 원소에 대해서 반복한다. 최대힙에 원소가 1개 남으면 종료. 

![image](https://user-images.githubusercontent.com/26478398/215319623-e795abe9-2d5e-4ed7-a069-43dc2a7d9f79.png)

### ✨선택 정렬
```
array = [2, 3, 1, 4]
for i in range(len(array)):
    min_index = i # index of the smallest element
    for j in range(i+1, len(array)):
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap
```

<details><summary><b>👀문제풀이</b></summary>

* 정렬 > 소트인사이드 ▪▪
[문제](https://www.acmicpc.net/problem/1427) ▪▪ [풀이](/sort/sortinside.py)

<img src="https://img.shields.io/badge/programmers-blue"/>

* 정렬 > H-Index ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/42747) ▪▪ [풀이](/sort/hindex.py)
* 정렬 > 가장 큰 수 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3) ▪▪ [풀이](/sort/biggestnumber.py)

<img src="https://img.shields.io/badge/codility-orange"/>

* triangle ▪▪
[문제](https://app.codility.com/programmers/lessons/6-sorting/triangle/start/) ▪▪ [풀이](/sort/triangle.py)

</details><br>

## ✨완전 탐색

### 방향벡터
```
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 현재위치
x, y = 2, 2

# 다음위치
for i in range(4):
	nx = x + dx[i]
	ny = y + dy[i]	
```

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/programmers-blue"/>

* 완전탐색 > 카펫 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/42842) ▪▪ [풀이](/bruteforce/carpet.py)
* 2023 KAKAO BLIND RECRUITMENT > 이모티콘 할인행사 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/150368) ▪▪ [풀이](/bruteforce/emoticonsale.py)

</details><br>

## 이분 탐색, 이진 탐색, Binary Search

: 탐색 범위를 절반으로 줄여가면서 원하는 숫자(target)를 찾기

- 완전 탐색으로 풀다가 경우 시간 초과가 나는 경우 이분탐색으로 해결하면 되는 경우가 많다.
- O(N)이 걸릴 탐색을 O(logN)으로 줄여준다.
- Parametric Search는 주어진 범위 내에서 원하는 값 또는 조건에 가장 일치하는 값을 찾아내는 알고리즘이다. 이런 형태의 문제를 이진 탐색으로 해결한다.

### 유의사항
- 타겟을 찾을 때에는 배열안의 값은 반드시 정렬되어있어야 한다.

```
left, right = 0, max(arr)

while left <= right:
    mid = (left + right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        right = mid-1
    else:
        left = mid+1

return -1 #찾지 못했을 때
```

### 
left(a, x)
- 정렬된 a에 x를 삽입할 위치를 리턴한다.
- x가 이미 있으면 x위치의 앞 위치를 리턴한다.

### bisect_right(a, x)
- x가 이미 있으면 x위치의 뒤 위치를 반환한다.

=> 값이 없을 때는 같은 값 리턴
=> 값이 있을 때 왼쪽을 리턴할지 vs 오른쪽을 리턴할지 차이

```
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x)) // 2
print(bisect_right(a, x)) // 4
```

### 값이 특정 범위에 속하는 데이터 개수 세기
```
from bisect import bisect_left, bisect_right

def count_by_range(a, left_val, right_val):
    right_index = bisect_right(a, right_val)
	left_index = bisect_left(a, left_val)
	return right_index - left index
	
a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4)) # 값이 4인 개수 -> 2
print(count_by_range(a,-1,3)) # 값이 -1 ~ 3인 개수 -> 6
```


<details><summary><b>👀문제풀이</b></summary>

* 예산 ▪▪
[문제](https://www.acmicpc.net/problem/2512) ▪▪ [풀이](/binary/budget.py)

<img src="https://img.shields.io/badge/programmers-blue"/>

* 이분탐색 > 입국심사 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/43238) ▪▪ [풀이](/binary/immigration.py)
* 2020 KAKAO BLIND RECRUITMENT > 가사 검색 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/60060?language=python3) ▪▪ [풀이](/binary/searchlycies.py)
* 징검다리 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/43236?language=python3) ▪▪ [풀이](/binary/steppingstone.py)

</details><br>

## 탐욕법 (Greedy)

: 그때 그때 상황에서 최적해가 전체 최적해가 된다는 원리

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/programmers-blue"/>

* 체육복 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/42862) ▪▪ [풀이](/greedy/gymsuit.py)

<img src="https://img.shields.io/badge/leetcode-green"/>

* Best Time to Buy and Sell Stock with Transaction Fee ▪▪
[문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/) ▪▪ [풀이](/greedy/besttimeinstock.py)
* Partition Array Into Three Parts With Equal Sum ▪▪
[문제](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/) ▪▪ [풀이](/greedy/partswithequalsum.py)
* Assign Cookies ▪▪
[문제](https://leetcode.com/problems/assign-cookies/description/) ▪▪ [풀이](/greedy/assigncookies.py)


<img src="https://img.shields.io/badge/codility-orange"/>

* MaxNonoverlappingSegments ▪▪
[문제](https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/start/) ▪▪ [풀이](/greedy/maxnonoverlappingsegments.py)

</details><br>


## 동적계획법 DP (Dynamic Programming)
- 완전 탐색으로 풀었을 때 시간초과가 나는 경우 DP를 이용한다.
- 문제에서 구하려고 하는 부분을 배열로 선언한다
- 조건이 여러개인 경우에는 2차원 배열을 선언한다
- ex) 구간을 구하는 문제는 A[i]를 끝점으로 하는 수열의 최장거리 또는 A[i]를 시작으로 하는 수열의 최장 길이로 선언한다.

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/programmers-blue"/>

* 동적계획법(Dynamic Programming) > 정수 삼각형 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/43105) ▪▪ [풀이](/dp/inttriangle.py)
* 동적계획법(Dynamic Programming) > N으로 표현 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42895) ▪▪ [풀이](/dp/nreturn.py)
* 동적계획법(Dynamic Programming) > 도둑질 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42897) ▪▪ [풀이](/dp/thievery.py)
* 연속 부분 수열 합의 개수 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=python3) ▪▪ [풀이](/dp/circlesum.py)
* 동적계획법(Dynamic Programming) > 등굣길 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3) ▪▪ [풀이](/dp/waytoschool.py)
* 코딩테스트 연습 > Summer/Winter Coding(~2018) > 스티커 모으기(2) ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/12971?language=python3) ▪▪ [풀이](/dp/getsticker.py)

<img src="https://img.shields.io/badge/leetcode-green"/>

* Unique Paths ▪▪
[문제](https://leetcode.com/problems/unique-paths/) ▪▪ [풀이](/dp/uniquepath.py)
* Longest Increasing Subsequence ▪▪
[문제](https://leetcode.com/problems/longest-increasing-subsequence/) ▪▪ [풀이](/dp/lis.py)
* Word Break ▪▪
[문제](https://leetcode.com/problems/word-break) ▪▪ [풀이](/dp/wordbreak.py)
* Is Subsequence ▪▪
[문제](https://leetcode.com/problems/is-subsequence/) ▪▪ [풀이](/dp/issubsequence.py)
* Maximum Subarray ▪▪
[문제](https://leetcode.com/problems/maximum-subarray/) ▪▪ [풀이](/dp/maximumsubarray.py)
* Count Number of Teams ▪▪
[문제](https://leetcode.com/problems/count-number-of-teams/description/) ▪▪ [풀이](/dp/countteams.py)

<img src="https://img.shields.io/badge/codility-orange"/>

* FibFrog ▪▪
[문제](https://app.codility.com/c/run/trainingHEAFCC-XPS/) ▪▪ [풀이](/dp/fibfrog.py)

</details><br>

## 깊이 우선 탐색 DFS / 넓이 우선 탐색 BFS

### ✨DFS
- 한가지 정점과 연결된 모든 정점을 탐색해야하는 경우
- 경로를 찾아야하는 경우
- 사이클이 존재하는 경로를 찾는 경우

### 구현 방법
- 인접행렬, stack 자료구조
- 인접행렬, 재귀함수
- 인접리스트, stack 자료구조
- 인접리스트, 재귀함수

### 구현 절차
1. 탐색 시작 노드를 스택에 삽입 후 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

### 인접행렬 스택으로 구현 1)
```
n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
    stack = [i]
    
    while stack:
        value = stack.pop()
        
        if not visited[value]:
            visited[value] = True
        
        for c in range(len(matrix[value])-1, -1, -1):
            if matrix[value][c] == 1 and not visited[c]:
                stack.append(c)
                
dfs(matrix, v, visited)
```

### 인접행렬 재귀함수로 구현 2)
- 코드가 간결하다.
```
n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
  visited[i] = True
  print(i, end=' ')
  for c in range(len(matrix[i])):
    if matrix[i][c] == 1 and not visited[c]:
      dfs(matrix, c, visited)
dfs(matrix, v, visited)
```

### 인접리스트 stack 구현 2)
- 인접리스트를 이중 list로 구현했습니다.
- 인접행렬과 마찬가지로 n+1개의 노드를 만들었습니다.
- 인접행렬에서 모든 행을 반복문으로 확인하여 연결정보를 얻은 것과는 달리, graph[value] 한번 만으로 모든 연결 정보를 가져온다.

```
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m): 
  v1, v2 = map(int, sys.stdin.readline().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

def dfs(graph, i, visited):
  stack = [i]
  visited[i] = True
  
  while stack:
    value = stack.pop()
	
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
	  
    for j in graph[value]:
      if not visited[j]:
        stack.append(j)

for i in graph: # 앞서 인접행렬에서 거꾸로 순회했던 이유가 같습니다.
	i.reverse()
  
dfs(graph, v, visited)
```

### 인접리스트 재귀함수 구현

```
n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  graph[f].append(t)
  graph[t].append(f)

def dfs(graph, i, visited):
  visited[i] = True
  print(i, end=' ')
  
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)

dfs(graph, v, visited)
```

### 스택으로 구현 2) "set, stack, root, visited"
```
graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root = 1

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

dfs(graph, root)
```

### 재귀로 구현
- 방문 체크 배열 선언
```
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

- 파이썬은 재귀호출 횟수가 1000회로 제한되어 sys 모듈의 setrecursionlimit()으로 제한을 늘려줌
```
import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    for j in range(1, N+1):
        if adf[i][j] and not chk[j]:
            chk[j] = True
            dfs(j)
```

### 양방향 그래프 구현 "set, deque, root, visited, sort(reverse=True)"
```
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)
```

### connected component 구하기
```
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
```

### 사이클 찾기
- 방문 체크 배열 선언
- 사이클 체크 배열 선언
```
stack = [0]
while stack:
    n = stack.pop()
    for i in adj[n]:
        if not i in visited:
            stack.append(i)
    visited.append(n)
return visited
# visited에 중복된 노드가 있을 경우 사이클이 존재한다고 판단!
```

### ✨백트래킹 backtracking
원하는 값과 불일치 하는 부분이 있으면 더이상 탐색하지 않고 전 단계로 돌아간다.
- Promising: 트리구조 기반으로 DFS 탐색하면서 조건에 부합하는지 체크
- Pruning: 조건에 맞지 않는 노드는 가지치키한다.
ex) 미로 찾기 (트리 탐색 문제로 해석), n-queens

```
n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

def dfs(depth, n, m):
  if depth == m:
    print(' '.join(map(str, answer)))

  for i in range(1, n+1):
    # 방문하지 않았을 경우
    if not visited[i]:
      visited[i] = True
      answer.append(i)
      dfs(depth+1, n, m) # depth 1 증가, 다음 노드
      visited[i] = False
      answer.pop()

dfs(0, n, m)
```

### ✨BFS
- 최단 거리를 구해야하는 경우
- 최단 거리를 구하되 조건이 여러개 존재하는 경우 (방문한 지정도 다시 방문 가능)
- 큐 자료구조 이용

### 구현 방법
- 인접행렬, queue 자료구조
- 인접리스트, queue 자료구조


### 구현 절차
1. 탐색 시작 노드를 큐에 삽입하고 방문처리
2. 큐에서 노드를 꺼내 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 한다.
3. 2번을 수행할 수 없을 때까지 반복 while


### 인접행렬, queue 자료구조

```
n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1
  
from collections import deque

def bfs(matrix, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for c in range(len(matrix[value])):
        if matrix[value][c] == 1 and not visited[c]:
          queue.append(c)
```

### 인접리스트, queue 자료구조
```
n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)

from collections import deque

def bfs(graph, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()

    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for j in graph[value]:
        queue.append(j)

bfs(graph, v, visited)
```


### 큐로 구현 1) "deque, start, visited"
```
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보 (2차원 리스트) 첫번째는 비워둔다.
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보 (1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)
```

### 큐로 구현 2) "set, deque, root, visited"
```
from collections import deque

graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root = 1

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
    
bfs(graph, root)
```

### 양방향 그래프 구현 "set, deque, root, visited, sort"
```
from collections import deque

graph = {1:[2,3,4], 2:[1,4], 3:[1,4], 4:[1,2,3]}
root = 1

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)
    
BFS(graph, root)
```

### 미로 최단 거리 찾기
```
from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

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

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    answer = graph[-1][-1]
    return answer
```

### 방향 그래프 순환 탐지

1. 최초에 내차수가 0인 정점을 모두 찾아 각 정점을 큐에 넣는다.
2. 큐에서 하나씩 빼서 방문 완료 처리하고 방문 완료 정점의 수를 1 늘리고, 해당 정점의 인접 정점의 내차수를 1씩 뺀 다음, 인접 정점 중 내차수가 0이된 것만 큐에 넣는다.
3. 큐가 빌 때까지 위 ⒝를 지속 반복한다.
4. 큐가 비었는데 전체 정점의 수와 방문 완료된 정점의 수가 다르다면 Cycle이 있는 것이다.

### 무방향 그래프 순환 탐지
무방향 그래프는 상호 연결되어 있기 때문에 방향 그래프에서 순환 탐지 하듯이 탐지를 시도하면 무조건 순환이 있는 것으로 탐지된다.

1. 그래프를 만들고 BFS 탐색 함수를 생성하여 현재 정점, 방문 여부 배열을 전달한다.
2. 현재 탐색 정점을 방문 완료로 표시하고 parent배열을 따로 생성한 뒤, 최초 탐색 정점의 parent는 -1로 저장
  - parent는 현재 노드와 이어진 이전에 탐색된 노드가 저장된 배열
3. BFS 탐색을 위해 큐를 생성하고 최초 탐색 수행 정점을 큐에 넣는다.
4. 큐가 비어 있지 않은 동안 반복문을 수행하며 큐의 정점을 하나씩 빼고 방문되지 않은 인접 정점들을 탐색한다.
5. 인접 정점이 기 방문 상태이며 parent가 현재 정점 값이 아니라면 순환 있음으로 결과값 반환


<details><summary><b>👀문제풀이</b></summary>

* DFS와 BFS ▪▪
[문제](https://www.acmicpc.net/problem/1260) ▪▪ [풀이](/dfsbfs/dfsbfs.py)
* 서울 지하철 2호선 ▪▪
[문제](https://www.acmicpc.net/problem/16947) ▪▪ [풀이](/dfsbfs/station2line.py)
* 연결 요소의 개수 ▪▪
[문제](https://www.acmicpc.net/problem/11724) ▪▪ [풀이](/dfsbfs/connectedcomponent.py)
* 미로 탐색 ▪▪
[문제](https://www.acmicpc.net/problem/2178) ▪▪ [풀이](/dfsbfs/searchmaze.py)
	
<img src="https://img.shields.io/badge/programmers-blue"/>

* 타겟 넘버 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3) ▪▪ [풀이](/dfsbfs/targetnumber.py)
* 게임 맵 최단거리 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3) ▪▪ [풀이](/dfsbfs/gamemap.py)

<img src="https://img.shields.io/badge/leetcode-green"/>

* Numbers With Same Consecutive Differences ▪▪
[문제](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) ▪▪ [풀이](/dfsbfs/samediffnum.py)

</details><br>

## ✨투포인터
: 구간을 구하기 위해 사용하는 알고리즘

- 완전 탐색으로 구간을 구할 수는 있지만 효율성 측면에서 사용한다.
- 배열의 인덱스를 가리키는 start와 end 포인터 두가지를 두고 조건에 맞춰 end 포인터를 ++1, start 포인터를 ++1 해나가는 방식
- 유형1) 대상 배열이 1개인 경우 / 유형2) 대상 배열이 2개인 경우

```
1. start와 end 포인터를 모두 0으로 초기화한다.
2. start 포인터가 배열의 범위를 벗어날때까지 반복한다.
3. sum < M, end++
4. sum >= M, start++
5. end 포인터가 배열의 범위를 벗어나면 start++
```

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/programmers-blue"/>

* 2020 카카오 인턴십 > 보석 쇼핑 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/67258) ▪▪ [풀이](/pointer/gemshop.py)

</details><br>

## ✨기타

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/programmers-blue"/>

* 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/72410) ▪▪ [풀이](https://github.com/nayoung240/algorithm/blob/main/newid.js)
[풀이2](/etc/newid.py)
* 위클리 챌린지 > 부족한 금액 계산하기 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/82612) ▪▪ [풀이](/etc/lackmoney.py)
* 위클리 챌린지 > 상호평가 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/83201) ▪▪ [풀이](/etc/evaluation.py)
* 스킬 체크 테스트 Level1 ▪▪
[문제](https://programmers.co.kr/skill_checks/403872) ▪▪ [풀이](/etc/caldate.py)
* 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 다단계 피라미드 ▪▪
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/77486?language=python3) ▪▪ [풀이](/etc/pyramid.py)

<img src="https://img.shields.io/badge/codility-orange"/>

* ChocolatesByNumbers ▪▪
[문제](https://app.codility.com/c/run/training5P4VES-W7D/) ▪▪ [풀이](/etc/chocolatesbynumbers.py)

</details><br>

## ✨성능

<details><summary><b>👀문제풀이</b></summary>

<img src="https://img.shields.io/badge/codility-orange"/>

* OddOccurrencesInArray ▪▪
[문제](https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/start/) ▪▪ [풀이](/performance/oddinarray.py)
* FrogRiverOne ▪▪
[문제](https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/start/) ▪▪ [풀이](/performance/frogreverone.py)
* MinPerimeterRectangle ▪▪
[문제](https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/start/) ▪▪ [풀이](/etc/minperimeterrectangle.py)
* Flags ▪▪
[문제](https://app.codility.com/c/run/trainingV34MU7-925/) ▪▪ [풀이](/etc/flags.py)

</details><br>


## sql
* 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 헤비 유저가 소유한 장소 ▪▪
[문제](https://programmers.co.kr/learn/courses/30/lessons/77487) ▪▪ [풀이](/sql/havyuser.sql)

<br>

## 코딩테스트 사이트
- 프로그래머스
  - 장점: 회사 기출 문제 모음 제공, 온라인 IDE 제공, 테스트케이스 추가 가능
- 백준 
  - 장점: 다양한 문제, 많은 풀이
- leetcode
  - 장점: 영어문제, 온라인 IDE 제공 
- codility
  - 장점: 영어문제, 온라인 IDE 제공, 성능시간 분석 제공 

<br><hr><br>

# 알아두면 쓸모있는?! 나만의 Cheat seat

## ✨입력 받기
### 여러줄 입력받을 때 타임아웃 걸리지 않으려면
```
import sys 
T = int(input()) 
for i in range(T): 
    a,b = map(int, sys.stdin.readline().split()) 
```

### 개행문자까지 입력받기
```
import sys
sys.stdin.readline().strip()
```

### 분리하여 입력받기
```
import sys
n = list(map(int, sys.stdin.readline().split()))
```

## ✨map(function, iterable)
- 리스트의 모든 원소에 각각 특정 함수를 적용할 때 사용한다.

### map을 사용하지 않으면 for문으로 번거로움
```
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)
```
### map을 사용할 때
```
myList = [1, 2, 3, 4, 5]

def add_one(n):
    return n + 1

result2 = list(map(add_one, myList))  # map반환을 list 로 변환
```

### map, lamda 함수(이름없는 함수) 이용
```
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
```

## ✨counter()
- return dictionary형 {객체값 : counter수}
- counter 객체 간 더하기, 빼기, 교집합, 합집합 연산 가능
- 시간 복잡도: O(N)
  - for문을 통해서 count하면 시간복잡도가 O(N**2) 이지만 counter는 count를 n번 하는 것이라 빠르다.


```
from collections import Counter
answer = Counter(p) - Counter(c)
answer = set(Counter(p)) - set(Counter(c))
answer = Counter(Counter(p).values()) - Counter(Counter(c).values())
```

## ✨소수점
```
round(number) # 반올림

import math
math.ceil(number) # 올림
```


## ✨순열
- permutations(): 하나의 리스트에서 모든 조합 계산(순서포함)
```
from itertools import permutations
a = list(permutations(arr, 2))
```

## ✨조합
- combinations(): 하나의 리스트에서 모든 조합 계산 (순서 상관 없이)
```
from itertools import combinations

a = combinations([2,1,3], 2)
print(list(a)) # [(2,1),(2,3),(1,3)]
```

- product(): 두개 이상의 리스트에서 모든 조합 계산
```
from itertools import product

a = product(*arr)
b = product(arr, repet=5)
```

## ✨피보나치 수열
```
def fibonacci(a):
    if a < 2:
        return a
    return fibonacci(a-2) + fibonacci(a-1)
```

## ✨ Max Consecutive Number Subsequence 최대 연속 부분 수열의 합
- 개념: 연속된 원소를 더한 부분 수열의 최대값

### 알고리즘
- 현재 합
- 합의 최댓값
1. 수의 합을 반복적으로 구한다.
2. 이 때 합이 음수이면 현재 합은 0이되고 그 다음 수부터 다시 시작한다.
3. 합의 최댓값을 도출한다.

## ✨ LIS(Longest Increasing Subsequence)  최장 증가 부분 수열 / LCS(Longest Common Subsequence) 최장 공통 부분 수열

- 개념은 간단하지만 어떨 때 해당 방법을 활용할지 판단이 어렵다.
- 기본적으로 부분 수열 구하기에 DP를 얹은 형태
- DP로 풀면 O(N^2) 이기때문에 이분탐색을 활용해 O(logN)으로 최적화 가능하다.

```
import bisect

def lengthOfLIS(nums):
    arr = []
        
    for num in nums:
        insertion_pos = bisect.bisect_left(arr, num)
            
        if insertion_pos == len(arr):
            arr.append(num)
        else:
            arr[insertion_pos] = num
        
    return len(arr)
```

## ✨set 집합 자료형
- 중복을 제거한다.
- 추가: add()
- 제거: remove()
- 교집합: list(set(A) & set(B))
- 합집합: list(set(A) | set(B))
- 차집합: list(set(A) - set(B))

## ✨ 우선순위 큐
- N번째 요소 구하기 (큐의 크기를 N으로 유지한 뒤 N+1개가 들어올 때 가장 작은 요소와 비교
- 중앙값 구하기 (두개의 우선순위 큐 이용)
- 2, 5, 8, 11 ... 초기값을 큐에 넣고 하나씩 뽑으면서 연산을 진행한 후 N번째 요소 구하기


## ✨ Dijkstra 다익스트라 알고리즘
- 최단 거리 구하기 (노드, 가중치를 가진 간선)
- 한 지점에서 다른 지점까지 최단 경로
- 우선순위 큐 heapq : 우선순위가 가장 높은 데이터를 가장 먼저 꺼낸다
- 거리 리스트, 방문여부 리스트

1. 출발 노드 설정한다
2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다
4. 해당 노드를 거쳐서 특정한 노드로 가능 경우를 고려하여 최소 비용을 갱신한다
5. 3~4번 반복
```
import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0            # 시작노드->시작노드 거리 기록

    while q:
        dist, node = heapq.heappop(q)

        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue

        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]   # 시작->node거리 + node->node의인접노드 거리
            if cost < distance[next[0]]:      # cost < 시작->node의인접노드 거리
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])
```

## ✨분할정복
```
array = [2, 3, 1, 4]
def quick_sort(array):
    #quit if list has one or less elements
    if len(array) <= 1:
        return array
    
    pivot = array[0] # first element as pivot
    tail = array[1:] # list accept pivot
    left = [x for x in tail if x <= pivot] # left side
    right = [x for x in tail if x > pivot] # right side
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
```


## ✨ Trie 트라이 알고리즘
: 문자열을 찾을 때 사용하는 알고리즘

- Tree 형태로 저장하여 검색 속도 향상을 추구한다.
- 시간복잡도: O(L)  // 문자열 길이 만큼
- 이론적으로는 좋지만 해시, 이진 검색 트리에 비해 훨씬 느림. 일반적인 상황에서는 해시나 이진 검색 트리를 사용하는게 좋고 트라이를 활용해야할 때도 있다.

1. 문자들을 저장할 Node클래스를 생성해준다.
```
class Node(object):
    def __init__(self, key):
        self.key = key          # 해당 문자를 key값으로 가짐
        self.children = {}      # 자식노드를 딕셔너리형태로 저장
```
2. 빈 Node를 생성하고 self.head로 가리킨다.
3. insert 메소드 (삽입)
4. search 메소드 (탐색)
```
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head
 
        for char in string:
            if char not in cur_node.children:
                # 해당문자가 자식노드에 없을 경우 노드 추가
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
 
        cur_node.children['*'] = True       # 문자열의 마지막에 '*' 삽입
        
    def search(self, string):
        cur_node = self.head
 
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
 
        # 트리의 끝까지 갔을때 마지막노드의 자식이 '*'이면 True 리턴
        if '*' in cur_node.children:
            return True
```

```
trie = Trie()
trie.insert(s)
a = trie.search('leetcode')
```

## ✨ 메모이제이션 Memoization

동일한 계산을 여러 번 반복해야 하는 경우, 한 번 계산한 결과를 메모리에 저장해 두었다가 필요한 경우 꺼내서 사용함으로써 중복 계산을 방지하는 기법.

- 동적 계획법의 핵심이 되는 기술
- 메모리라는 공간 비용을 투입해서 계산에 소요되는 시간 비용을 줄이는 방법이다.
- 재귀의 단점: 값이 커지면 연산이 많아진다. -> 메모이제이션으로 해결한다.

ex) 피보나치 수열 - m이라는 리스트에 이미 계산한 피보나치 값을 넣어두고 필요에따라 가져온다.
```
max_value=int(input())
m=[0]*max_value

def fibonacci(a):
    if a < 2:
        return a
    elif m[a]:
        return m[a]
    m[a] = fibonacci(a-1)+fibonacci(a-2)
    return m[a]
```

## ✨유클리드 호제법 (최대 공약수 구하기)
큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다. 큰 수를 작은 수로 계속 나누어서, 나누어 떨어질 때까지 반복한다. 나누어 떨어질 때(나머지가 0일 때), 나누는 수가 최대공약수이다

```
from math import gcd

a = math.gcd(21, 14) # 최대 공약수
a = 21 * 14 // math.gcd(21, 14) # 최소 공배수
```

## ✨유니온파인드
: 현재 노드들이 같은 그룹에 속해 있는지 확인하고 같은 그룹으로 만드는 병합이 필요할 때 사용하는 알고리즘

- 크루스칼 알고리즘과 더불어 같이 많이 사용된다.
- find : 부모 노드를 찾을때까지 재귀적으로 호출
- union : 두 원소의 부모 노드를 찾고 번호가 큰 노드가 번호가 작은 노드의 부모를 가리키도록 한다. (부모테이블을 항상 가지고 있어야 한다.)

### find
```
par = [ -1 for i in range(N + 1) ]  # 루트를 담을 배열

def find(x):    # 루트를 찾아주는 함수
    if par[x] < 0:  # 아직 루트가 없다면
        return x    # 자기 자신이 루트  => 아직 연결된 적이 없음
    par[x] = find(par[x])   # 자신의 부모를 부모->부모 를 재귀로 루트 부모를 찾음
    return par[x]   # 루트 부모를 리턴
```

### union
```
def union(a, b):    # union 두 집합을 연결해주는 함수
    a, b = find(a), find(b) 
    if a == b:  # 루트 부모가 같다면 같은 집합 => 이미 연결 관계
        return False
    par[b] = a  # 부모 노드를 통일시켜 하나의 집합으로 병합
    return True
```

## ✨크루스칼 알고리즘
: MST(Minimum Spanning Tree)를 구하기 위한 알고리즘

- N개의 노드로 이루어진 그래프가 주어졌을 때 N-1개의 간선을 이용한 최소 가중치의 트리를 구할 때 사용한다.
- 유형1) 간선이 모두 주어지는 경우, 유형2) 간선이 주어지지 않는 경우 -> 모든 간선을 직접 구해야한다면 시간 초과가 날 수 있다. 조건을 정렬하여 최소 간선만 선택할 수 있도록 해야한다.


```
1. 간선들을 모두 오름차순 정렬한다.
2. 가중치가 가장 작은 간선부터 선택하면서 사이클이 생기지 않는 경우 해당 간선을 선택한다.
3. N-1개의 간선이 선택될때까지 반복
```

## ✨트리의 지름 구하기
: 가장 멀리 떨어져있는 두 노드 사이의 depth 구하기

- dfs 알고리즘 2번 수행
  1. 임의의 정점에서 dfs 알고리즘을 수행해 가장 멀리 떨어져있는 노드 구하기
  2. 1번에서 구한 노드를 대상으로 다시 dfs를 수행해 가장 멀리 떨어져 있는 노드 구하기 -> 

## ✨기타


### 리스트 컴프리헨션 - 2차원 리스트를 초기화할 때 유의사항
* a = [[0] * m] * n -> 전체 리스트 안에 포함된 리스트가 모두 같은 객체로 인식되므로 주의
* 좋은 예시) n X m 크기의 2차원 리스트 -> [[0] * m for _ in range(n)]

### 2차원 배열을 1차원 배열로 합치기
```
sum(matrix,[])
```

### 여러 그룹의 데이터를 루프를 한 번만 돌면서 병렬 처리 가능 (묶기)
```
zip([1,2,3],['a','b','c']) # (1,'a'),(2,'b'),(3,'c')
```

### for문 돌면서 popleft하게되면 에러가 발생한다.
```
import copy
for i in copy.deepcopy(workday):
```

### 리스트 맨앞에 요소 추가하기 - insert( )
```
arr.insert(0, tmp)
```

### deque
- popleft() 필요할 때 효율성 높음
```
from collections import deque 
workday = deque()
```

### defaultdict(int) 를 사용하면 if 미리 존재하는지 체크안해도 된다.
- dictionary의 초기값은 0으로 지정되기때문이다.
```
for j in strarr:
    if j in counts:
        counts[j] += 1
    else:
        counts[j] = 1
```
```
from collections import defaultdict
counts = defaultdict(int)
for j in strarr:
    counts[j] += 1
```

### 리스트 요소들 사이에 sep 구분자를 넣어 출력하기  
```
print(*answer, sep='\n')
```

### 튜플을 문자열로 변환하기
```
''.join(튜플)
```

### 숫자 리스트를 문자열로 변환하기
```
''.join(map(str,리스트))
```

### 윤년은 2월이 29일이다.

### 문자열 정해진 수를 0으로 채우기
```
'8'.zfill(3) #008
```

### 2진수, 8진수, 16진수 변환
```
format(N, 'b') # 2진수 Binary format
format(N, 'o') # 8진수 Octal format
format(N, 'x') # 16진수 Hexadecimal format
```

### 특정 문자열에서 찾는 문자열의 모든 인덱스 찾기
- finditer(패턴, 문자열, 플래그)
```
for text in re.finditer('1', binaryNum):
    now = text.start()
```

### for문 거꾸로 출력하기
```
st = [1, 2, 3, 4, 5]

for f in range(len(st)-1, -1, -1):
  print(st[f]) # 5, 4, 3,,,
```

### index 함수 try catch 예외처리

```
idx = 'f'
t = 'qweqwe'

try:
    index = t.index(idx)
except ValueError: 
    return False
```

### 약수 구하기
- 제곱근을 사용해서 범위를 좁혀야 효율적이다.

```
for i in range(1, int(N ** (1 / 2)) + 1):
    if N % i == 0:
        data.add(i)
        data.add(N // i)
```

### 시간 복잡도 관련 Tip

- 정렬은 O(nlogn)이며 `sort()` 함수를 이용한다.
- hashtable의 시간복잡도는 O(1)이다. 보통 문제에서 주어지는 크기 n의 데이터에 하나하나 접근하여 hashtable을 구축하면 O(n)의 시간복잡도가 걸린다.
- 반복문 또는 재귀 함수가 재호출될때마다 탐색해야할 데이터 크기가 절반씩 줄어들기 때문에 시간복잡도 O(logn)이 된다.
- 길이가 n인 배열을 heap으로 만들면 O(nlogn)이 걸린다.
  - `push()` : O(logn), `pop()` : O(logn)
- 문제의 제약조건을 보고 시간복잡도에 데이터의 크기 N을 넣어서 나온 값이 1억이 넘으면 시간 제한 초과할 가능성이 있다.
  - O(n^2) 일때 10^4^2 은 1억이된다.

