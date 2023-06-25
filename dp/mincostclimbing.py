'''
Return 맨 끝 배열에 가기 위한 최소 비용.

누군가의 효율성 좋은 코드
시간복잡도: O(N)
공간복잡도: O(0)
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costlen = len(cost)
      
        for i in range(2, costlen):
            cost[i] += min(cost[i-2], cost[i-1])
        
        return min(cost[costlen-2], cost[costlen-1])
