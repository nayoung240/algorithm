'''
그리디 알고리즘
- 갯수를 나눠서 조합한 경우 -> 타임아웃 발생
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)

        if s%3 != 0:
            return False

        each = s/3
        temp, found = 0, 0

        for i in range(len(arr)):
            temp += arr[i]
            
            if temp == each:
                temp = 0
                found += 1
                
        return True if found >= 3 else False
