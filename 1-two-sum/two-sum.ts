function twoSum(nums: number[], target: number): number[] {
  let lookup = new Map() 
  for (let i = 0; i<nums.length;i++){
     if(lookup.has(target-nums[i])){
        if ( lookup.get(target-nums[i]) !== i){
            return [lookup.get(target-nums[i]),i]
        }
     }
     else{
        lookup.set(nums[i],i)
     }
  }
};