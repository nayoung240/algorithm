'''
동적 계획법
현재 상태가 가질 수 있는 가장 큰 이익을 저장하며 마지막 상태에서 가질 수 있는 가장 큰 이익값을 반환한다.
시간복잡도: O(N)
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        hold = -math.inf # -inf

        for price in prices:
            sell = max(sell, hold + price)
            hold = max(hold, sell - price - fee)
            print(sell, hold)
        return sell


'''
그리디
'''
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        ans = 0
        minimum = prices[0]

        if n < 2:
             return 0

        for i in range(1, n):
            print('start', prices[i],  minimum)

            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
            print(minimum, ans)

        return ans
