class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;

        for(int i =0;i<nums.size();i++){
            int curr = target - nums[i];
            if (m.find(curr)!= m.end()){
                vector<int> ret;
                ret.push_back(m[curr]);
                ret.push_back(i);
                return ret;
            }
            else{
                m[nums[i]] = i;
            }
        }
        return {};
    }
};