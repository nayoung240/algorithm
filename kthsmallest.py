import itertools

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        merged = list(itertools.chain.from_iterable(matrix))
        sortarr = sorted(merged, reverse=False)
        return(sortarr[k-1])
