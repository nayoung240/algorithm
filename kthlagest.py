'''
sort(): 리스트 원본값을 수정한다, 리턴값은 None
sorted(): 리스트 원본값은 그대로, 리턴값은 정렬값

중복제거&정렬하기: sorted(set(nums), reverse=True)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = sorted(nums, reverse=True)
        return l[k-1]
