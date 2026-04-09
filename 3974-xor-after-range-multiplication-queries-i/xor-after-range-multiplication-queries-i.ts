function xorAfterQueries(nums: number[], queries: number[][]): number {
    for (let i = 0; i<queries.length;i++){
        let [l,r,k,v] = queries[i]
        let idx = l
        while(idx<=r){
            nums[idx] = (nums[idx]*v)%(7+10**9)
            idx+=k
        }
    }
    let ret  = 0
    for(let i = 0;i<nums.length;i++){
        ret ^=nums[i]
    }
    return ret
};