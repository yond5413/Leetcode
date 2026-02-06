class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        nums.sort()
        n = len(nums)
        big = float("-inf")
        while(r<n):
            if nums[r]<=nums[l]*k:
                print("wooooo")
                r+=1
                big = max(big,(r-l))
            else:
                l+=1
        if big == float("-inf"):
            big = r-l+1
        print(f"l:{l},r{r}")
        return n-big
            