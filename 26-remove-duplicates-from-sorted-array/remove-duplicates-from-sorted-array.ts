function removeDuplicates(nums: number[]): number {
    let k = 0
    for (let i=0;i<nums.length;i++){
        if (i===0 || nums[i-1]===nums[i]){
            k = i===0 ? k+1: k
            continue 
        }
        nums[k] = nums[i]
        k++
    }
    return k
};