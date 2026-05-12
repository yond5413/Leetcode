function majorityElement(nums: number[]): number {
    let freq = new Map()
    const n  =nums.length
    for (let i = 0;i<n;i++){
        if (freq.has(nums[i])){
            freq.set(nums[i],freq.get(nums[i])+1)
        }
        else{
            freq.set(nums[i],1)

        }
    }
    for (const k of freq.keys()){
        if (freq.get(k) >= n/2){
            return k
        }
    }
};