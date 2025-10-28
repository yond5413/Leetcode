function productExceptSelf(nums: number[]): number[] {
    let n = nums.length
    let pre =  Array(n).fill(1);
    for (let i = 1;i<n;i++){
        pre[i] = pre[i-1]*nums[i-1]
    }
    let post = 1;
    let ret = Array(n).fill(0)
    for (let i = n-1; i>=0;i--){
        ret[i] = post*pre[i]
        post*=nums[i]
    }
    return ret;  
};