function removeElement(nums: number[], val: number): number {
    let ret = 0
    let l = 0
    let n = nums.length
    for (let r = 0; r<n;r++){
        if (nums[r] != val){
            nums[l] = nums[r]
            l++
            ret++
        }
    }
    return ret
};