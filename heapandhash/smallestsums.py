'''
모든 탐색을 하면 메모리 초과된다.
'''
class Solution:
    import heapq

    # 두쌍 제일 작은거 k개 리스트 return
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        h = []
        cnt = 0

        for i in nums1:
            for j in nums2:
                heappush(h, (i+j, i, j))

        while h and cnt < k:
            b = heappop(h)
            answer.append([b[1], b[2]])
            cnt += 1

        return answer

'''
누군가의 정답
핵심 : last = k//(i+1)
'''
class Solution:
    import heapq

    # 두쌍 제일 작은거 k개 리스트 return
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []

        if not nums2 or not nums1: 
            return answer

        heap = []
        heapq.heapify(heap)

        for i, num1 in enumerate(nums1[:k]):
            last = k//(i+1)

            for num2 in nums2[:last]:
                heapq.heappush(heap, [num1+num2, num1, num2])

        for x in heapq.nsmallest(k, heap):
            answer.append(x[1:])

        return answer
            
