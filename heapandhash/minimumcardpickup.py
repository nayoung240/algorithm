class Solution:
    '''
    Return 한번 나왔던 숫자가 또나올 때 최소의 길이가 되는 수
    '''
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        minLen = len(cards)

        # 중복된 수가 없을 경우
        if minLen == len(set(cards)):
            return -1
        
        for r in range(0, len(cards)):
            char = cards[r]

            # 기존에 나왔던 수일때
            if char in seen:
                # 답이될 길이 vs 현재 수의 간격 길이 중 작은 것
                minLen = min(minLen, r - seen[char] + 1) 
                
            seen[char] = r

        return minLen
