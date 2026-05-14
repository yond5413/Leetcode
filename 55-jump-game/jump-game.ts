function canJump(nums: number[]): boolean {
    let ret = 1;

    for (let i = 0;i<nums.length;i++){
        if (ret===0) return false
        ret = Math.max(ret-1,nums[i])
    }
    return true
};