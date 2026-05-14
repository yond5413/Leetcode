function jump(nums: number[]): number {
    let ret = 0
    let [l,r] = [0,0]
    let n = nums.length -1
    while(r<n){
        let max_jump = 0
        for(let i = l; i<r+1;i++){
            max_jump = Math.max(max_jump,i+nums[i])
        }    
        l = r+1
        r = max_jump
        ret++
    }
    return ret
};