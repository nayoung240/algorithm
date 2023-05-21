'''
왼쪽, 위를 누적하면서 정사각형이 될 수 있는지 판단한다.
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i, j)
                if matrix[i][j] == 1 and (i != 0 and j != 0):
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    print(matrix)

            count += sum(matrix[i])

        return count
