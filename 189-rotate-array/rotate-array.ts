/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  const n = nums.length
  const steps = k%n  
  if (steps===0) return;
    const rev = (arr:number[],l:number,r:number)=>{   
        while(l<r){
            [nums[l],nums[r]] = [nums[r],nums[l]]
            l++
            r--
        }

        return arr
    }
    nums = rev(nums,0,n-1)
    nums = rev(nums,0,steps-1)
    nums = rev(nums,steps,n-1)
};