function longestOnes(nums: number[], k: number): number {
    let ret = 0
    let l =0
    let r = 0
    let flips = 0
    while (r<nums.length){
        if (nums[r] != 1){
            flips++
        }
        while(flips>k){
            if (nums[l] !=1){
                flips--
            }
            l++
        }
        ret = Math.max(r-l+1,ret)
        r++
    }
    return ret
};