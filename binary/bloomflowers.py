class Solution:
    '''
    Return 사람 index에 피어있는 꽃 수
    1) 꽃이 피어있는 배열 다 구하기 -> bloom = [0] * 10**9 -> memory 초과
    2) 사람을 기준으로 꽃 세기 -> Time Limit Exceeded 

    '''
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(a for a,b in flowers)
        end = sorted(b for a,b in flowers)
        
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
