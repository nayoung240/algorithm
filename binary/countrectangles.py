class Solution:
    '''
    Return 포인트를 포함하고 있는 직사각형의 수
    '''
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        answer = []
        rectangles.sort()
        length = defaultdict(list)

        for l, h in rectangles:
            length[h].append(l)

        for x, y in points:
            a = []

            for h in range(y, 101):
                b = len(length[h]) - bisect.bisect_left(length[h], x)
                a.append(b)
                
            answer.append(sum(a))

        return answer
        
