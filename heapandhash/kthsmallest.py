'''
itertools.chain.from_iterable(): 2차원 배열을 1차원배열로 만들기
'''
import itertools

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        merged = list(itertools.chain.from_iterable(matrix))
        sortarr = sorted(merged, reverse=False)
        return(sortarr[k-1])

'''
어려운 라이브러리 개선
sum(matrix,[])
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        merged = sum(matrix,[])
        sortarr = sorted(merged, reverse=False)
        return(sortarr[k-1])
