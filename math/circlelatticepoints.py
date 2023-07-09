class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()

        for x,y,r in circles:
            # 최소
            xmin = x - r
            ymin = y - r
            # 최대
            xmax = x + r
            ymax = y + r

            for i in range(xmin, xmax + 1):
                for j in range(ymin, ymax + 1):

                    # 피타고라스의 정리 빗변의 제곱은 나머지 두변의 제곱의 합과 같다.
                    if (x - i) ** 2 + (y - j) ** 2 <= r * r:
                        res.add((i,j))
        return len(res)
