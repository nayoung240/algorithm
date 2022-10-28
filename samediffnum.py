class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []

        def dfs(num, target):        
            # 다음 자리 숫자가 0~9 사이여야 한다.
            if target < 0 or target > 9:
                return

            numsum = num + str(target)
            
            # 자리수가 만족하면 종료
            if len(numsum) == n:
                answer.append(int(numsum))
                return           
            
            dfs(numsum, target + k)
            dfs(numsum, target - k)

        for first in range(1, 10):
            num = ''     
            dfs(num, first)
            
        
        return set(answer) # 중복제거
        
