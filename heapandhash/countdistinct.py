class Solution:
    # return 유일하고 p로 나눌 수 있는 수가 k개를 넘지 않는 subarray 수
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        answer = 0
        allSubList = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                subList = nums[i:j]
                cnt = 0
                
                for s in subList:
                    if s % p == 0:
                        cnt += 1

                # p로 나눌 수 있는 수가 k개를 넘으면 pass
                if cnt > k:
                    continue
                
                allSubList.add(tuple(subList)) # tuple 형태로 넣어야 set에 들어갈 수 있음
            
        return len(allSubList)
        
