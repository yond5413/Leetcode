class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        def inc(arr:List[int]):
            n = len(arr)
            for i in range(n-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True
        def dec(arr:List[int]):
            n = len(arr)
            for i in range(n-1):
                if arr[i]<=arr[i+1]:
                    return False
            return True
        for p in range(1,n):
            for q in range(p+1,n-1):
                if inc(nums[0:p+1]) and dec(nums[p:q+1]) and inc(nums[q:]):
                    return True
        return False