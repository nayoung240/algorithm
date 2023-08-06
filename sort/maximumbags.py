class Solution:
    '''
    Return 풀용량으로 채울 수 있는 가방 최대개수
    
    그냥 순서대로 계산하면 max로 못채움
    차이가 적게나는 순서대로 정렬 후 계산해야함
    '''
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer = 0
        
        # 차이가 작게 나는 순서대로 index 담기
        indices = sorted(range(len(capacity)), key=lambda i: abs(capacity[i] - rocks[i]))
        
        for i in indices:
            diff = capacity[i] - rocks[i]
            
            if diff == 0: # full
                answer += 1
                continue
                
            if additionalRocks >= diff:
                answer += 1
                additionalRocks -= diff

        return answer
