'''
나의 풀이
- 세로로 했을 때 숫자 리스트 구현에만 신경씀
- 이중for문 2번
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowcnt = len(grid)
        tmp = [[] for i in range(rowcnt)]
        answer = 0

        for i in range(rowcnt):
            for j in range(rowcnt):
                tmp[j].append(grid[i][j])

        for i in grid:
            for j in tmp:
                if i == j:
                    answer += 1

        return answer
   
'''
기막힌 2줄짜리 파이썬 답
dictionary 형을 이용하여 비교한다.
- Counter()
- tuple()
- zip(*args)를 해주면 이차원리스트를 열끼리 묶어준다.
- sum()
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = Counter(tuple(row) for row in grid)      
        return sum(freq[tuple(col)] for col in zip(*grid))

    
'''
원래 내 풀이에 zip을 응용해보기 - 코드에 가독성은 높아진듯하다
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        tmp = []

        # 이차원리스트를 열 기준으로 만든다.
        for i in zip(*grid):
            tmp.append(list(i))

        for i in grid:
            for j in tmp:
                if i == j:
                    answer += 1

        return answer
    
    
