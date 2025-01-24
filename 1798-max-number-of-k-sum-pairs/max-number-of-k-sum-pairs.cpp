#include <algorithm>
#include <vector>
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int ret = 0;
        int l = 0, r = nums.size()-1;
        while(l<r){
            if (nums[l]+nums[r] == k){
                ret +=1;
                r-=1;
                l+=1;
            }
            else if (nums[l]+nums[r] > k){
                r -=1;
            }
            else{
                l +=1;
            }
        }
        return ret;
    }
};