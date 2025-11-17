function longestSubarray(nums: number[]): number {
    let ret = 0;
    let l = 0
    let flip = 1
    for (let r = 0;r<nums.length;r++){
        if (nums[r]===0){
            flip--
        }   
        if (flip<0){
           
            while (flip<0){
                
                if (nums[l] ===0){
                    flip++
                }
                l++;
            }
        }
         ret = Math.max(r-l,ret)
    }
    return ret;   
};