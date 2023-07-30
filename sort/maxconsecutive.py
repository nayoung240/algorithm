class Solution:
    '''
    Return the maximum number of consecutive floors without a special floor.
    특별한 층이 없는 최대 연속 층수
    
    10의 5승.. -> 이분탐색인가! -> bisect_left 사용하면 될 것 같아 -> 뭐를 기준으로...

    이분탐색은 아니고 for문 한번에 해결하는것!!
    '''
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        res = special[0] - bottom
        
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
            
        return max(res, top - special[-1])
        
