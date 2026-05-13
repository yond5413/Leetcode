/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    const n = nums.length
    const rot = k%n
    if (rot == 0) return 

    let helper = (arr:number[],l:number,r: number) :number[]=>{
        while(l<r){
            let temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l++
            r--
            
        }
        console.log(arr)
        return arr
    }
    nums = helper(nums,0,n-1)
    nums = helper(nums,0,rot-1)
    nums = helper(nums,rot,n-1)
};