'''
dictionary 구현
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        
        cnt = collections.Counter(s)
        sort = sorted(cnt, key = cnt.get, reverse =True)    # <--- To sort 
        
        for i in sort:
            res+= i*cnt[i]         # e * 2 => ee
        
        return res
