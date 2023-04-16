class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list(set(list1) & set(list2))
        idx = {}
        minsum = 1000 * 2

        for i in range(len(list1)):
            if list1[i] in common:
                idx[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in idx:
                idx[list2[i]] = idx[list2[i]] + i
                minsum = min(minsum, idx[list2[i]])

        result = list(filter(lambda x : idx[x] == minsum, idx))

        return result

'''
다른 사람의 풀이
'''
def findRestaurantTwoDicts(self, list1, list2):
        dic1, dic2 = {}, {}
        res_sum = len(list1)+len(list2)
      
        for i, s in enumerate(list1):
            dic1[s] = i
            
        for i, s in enumerate(list2):
            if s in dic1:
                tmp_sum = dic1[s] + i
                dic2[tmp_sum] = dic2.get(tmp_sum, []) + [s]
                res_sum = min(tmp_sum, res_sum)
                
        return dic2[res_sum]
      
