function majorityElement(nums: number[]): number {
    let freq = new Map()
    for (let i = 0; i<nums.length;i++){
        if (freq.has(nums[i])){
            freq.set(nums[i], freq.get(nums[i])+1)
        }
        else{
            freq.set(nums[i],1)
        }
    }
const n  = nums.length
    for (const k of freq.keys()){
        //console.log(freq[k])
        if (freq.get(k) >= n/2){
            return k
        }
    }

}