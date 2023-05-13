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
