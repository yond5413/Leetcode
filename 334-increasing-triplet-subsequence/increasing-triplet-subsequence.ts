function increasingTriplet(nums: number[]): boolean {
    if (nums.length < 3)
    {
        return false;
    }
    let min1 = Infinity;
    let min2 = Infinity;
    for (let i = 0;i<nums.length;i++){
        if (min1>=nums[i]){
            min1 = nums[i]
        }
        else if (min2>=nums[i]){
            min2 = nums[i]
        }
        else{
            return true;
        }
    }
    return false;
};