'''
풀이 핵심 (수학)
- 해당칸 가는 경로 수 = 위의칸 가는 경로 수 + 왼쪽칸 가는 경로 수
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([0]*n)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # 해당칸 가는 경로 수 = 위의칸 가는 경로 수 + 왼쪽칸 가는 경로 수
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1] # 마지막 칸 경로 수
