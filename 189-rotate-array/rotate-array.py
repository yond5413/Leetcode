class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        steps = k%n
        if steps == 0:
            return 
        def rev(arr,l,r):
            while(l<r):
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
            return arr
        nums = rev(nums,0,n-1)
        print(nums)
        nums = rev(nums,0,steps-1)
        print(nums)
        nums = rev(nums,steps,n-1)