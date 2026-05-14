function maxSubArray(nums: number[]): number {
    let ret = -Infinity
    let curr = 0
    for (let i of nums){
        curr = Math.max(curr+i,i)
        ret = Math.max(curr,ret)
    }
    return ret
};