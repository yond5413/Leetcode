class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = [(nums2[i],nums1[i]) for i in range(n)]
        ret = float("-inf")
        pairs.sort(reverse = True)
        heap = []
        total = 0
        ret = float("-inf")
        for n2,n1 in pairs:
            heapq.heappush(heap,n1)
            total+=n1
            if len(heap)>k:
                total-=heapq.heappop(heap)
            if len(heap) == k:
                ret = max(ret,total*n2)
        return ret