class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rot = k%n
        if rot == 0:
            return
        def helper(arr,i,j):
            while(i<j):
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
            return arr
        nums = helper(nums,0,n-1)
        nums = helper(nums,0,rot-1)
        nums = helper(nums,rot,n-1)