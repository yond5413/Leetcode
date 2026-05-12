function removeDuplicates(nums: number[]): number {
    let k = 2
    for (let r = 2; r<nums.length;r++){
        if (nums[k-2]!=nums[r]){
            nums[k] = nums[r] 
            k++
        }
    }
    return k
};