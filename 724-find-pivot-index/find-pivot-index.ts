function pivotIndex(nums: number[]): number {
    let total = 0
    for (let i = 0;i<nums.length;i++){
        total+=nums[i]
    }
    let pre = 0;
    for (let i = 0;i<nums.length;i++){
        if (pre ==total-(nums[i]+pre)){
            return i;
        }
        pre +=nums[i]
    }
    return -1;
};