class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rot = k%n
        if rot == 0:
            return 
        
        def help(arr,l,r):
            i,j = l,r
            print(f"i:{i}, j:{j}")
            while(i<j):
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
            print(arr)
            return arr
        nums = help(nums,0,n-1)
        nums = help(nums,0,rot-1)
        nums = help(nums,rot,n-1)
        return