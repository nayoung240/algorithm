'''
시간초과
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        max_num = -100000

        for i in range(len(nums)):
            for cnt in range(len(nums[i:])+1):
                if i == i+cnt:
                    arr = nums[i]
                    sum_arr = nums[i]
                else:
                    arr = nums[i:i+cnt]
                    sum_arr = sum(arr)

                if max_num < sum_arr:
                    max_num = sum_arr
                    dp = arr

        return max_num
      
'''
답
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
