class Solution:
    '''
    Return 포인트를 포함하고 있는 직사각형의 수
    '''
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        length = defaultdict(list)
        
        for l, h in rectangles:
            length[h].append(l)
        
        return [sum(len(length[h]) - bisect.bisect_left(length[h], x) for h in range(y, 101)) for x, y in points]
