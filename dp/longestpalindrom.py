'''
나의 풀이
완전탐색으로 풀었더니 실행시간이 좋지 않다.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        maxlen = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                char = s[i:j+1]
                charlen = len(char)

                # 팰린드롬 체크
                if maxlen < charlen and char == char[::-1]:
                    answer = char
                    maxlen = charlen


        return answer

'''
다른 사람의 풀이
DP로 푼다. 이해하는게 어렵긴하지만 속도가 빠르다.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s)) ]

        for i in range(len(s)):
            dp[i][i]=1

        ans=s[0]

        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=1

                    if j-i+1 > len(ans):
                        ans=s[i:j+1]

        return ans
