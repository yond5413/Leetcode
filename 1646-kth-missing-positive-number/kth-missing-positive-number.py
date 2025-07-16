class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        visited = set(arr)
        for i in range(1,1001):
            if i not in visited:
                k-=1
            if k==0:
                return i
        return 1000+k