'''
LIS 알고리즘 

DP 풀이 
시간복잡도: O(n^2)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        ans = [1] * N
        
        for i in range(1, N):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, ans[j])
                    
            ans[i] = maxi + 1
        
        return max(ans)

'''
binary search 풀이 
bisect.bisect_left

시간복잡도: O(NlogN)
'''

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        
        for num in nums:
            insertion_pos = bisect.bisect_left(arr, num)
            
            if insertion_pos == len(arr):
                arr.append(num)
            else:
                arr[insertion_pos] = num
        
        return len(arr)
