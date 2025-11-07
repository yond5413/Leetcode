/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    if (nums.length>1){
        let l = 0
        for (let r = 0;r<nums.length;r++){
            if (nums[r]!=0){
            let temp = nums[l] 
            nums[l] = nums[r]
            nums[r] = temp
            l+=1
            }
        }
    }
};