class Solution:
    '''
    Return 가장 큰 비트연산 값을 만드는 조합 숫자 리스트 사이즈 
    10의 5승 -> 모든 조합 다 구하면 시간초과 발생 99퍼 

    이분탐색은 아니고 비트연산 큰값 구하기..
    '''
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0]*24

        for item in candidates:
            i = 0

            while item > 0:
                count[i] += (item&1)
                item >>= 1
                i+= 1
                
        return max(count)
        
