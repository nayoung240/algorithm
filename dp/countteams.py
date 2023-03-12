'''
어려움...
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        up = [0] * n
        down = [0] * n
        
        teams = 0
        
        for j in range(n):
            for i in range(j):
                if rating[i] < rating[j]:
                    up[j] += 1
                    teams += up[i]
                else:
                    down[j] += 1
                    teams += down[i]
        
        return teams
