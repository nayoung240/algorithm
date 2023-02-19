'''
틀린 tc
g = [1,2,3]
s = [3]
1이 나와야한다.

내림차순으로 풀어야하나 했는데 오름차순으로 풀면된다.
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i, j = 0, 0
        g.sort()
        s.sort()

        print(g,s)

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1

        return count
