function maxOperations(nums: number[], k: number): number {
    let ret = 0;
    let l = 0;
    let r = nums.length-1;
    nums.sort((a,b)=> a-b)
    while (l<r){
        let curr = nums[l]+nums[r]
        if (curr==k){
            l++;
            r--;
            ret++;
        }
        else if (curr>k){
            r--;
        }
        else{
            l++;
        }
    }
    return ret;

};