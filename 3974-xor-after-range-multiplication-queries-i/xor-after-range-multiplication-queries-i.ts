function xorAfterQueries(nums: number[], queries: number[][]): number {
    for (let i = 0; i<queries.length;i++){
        let [l,r,k,v] = queries[i]
        let idx = l
        while(idx<=r){
            nums[idx] = (nums[idx]*v)%(7+10**9)
            idx+=k
        }
    }
    const ret = nums.reduce((n,v)=>n^v,0)
    return ret
};