function findMaxAverage(nums: number[], k: number): number {
    let curr = 0;
    for (let i =0;i<k;i++){
        curr +=nums[i]
    }
    let ret = curr/k;
    let l = 0
    for(let r = k;r<nums.length;r++){
        curr+= nums[r]
        curr-= nums[l]
        l++
        ret = Math.max(curr/k,ret) 
    }
    return ret
};