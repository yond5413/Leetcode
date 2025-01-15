#include <vector>
#include <set>
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> ret; 
        set<int> visited1; 
        set<int> visited2; 
        /*
         populate sets,
         apparently cannot caste vector to set
        */
        for(int i = 0; i<nums1.size();i++){
            visited1.insert(nums1[i]);
        }
         for(int i = 0; i<nums2.size();i++){
            visited2.insert(nums2[i]);
        }
        /////////////////////
        vector<int> curr;
        for(int i = 0; i<nums1.size();i++){
            if (visited2.find(nums1[i]) == visited2.end()){
                
                visited2.insert(nums1[i]);
                curr.push_back(nums1[i]);
            }
        }
        ret.push_back(curr);
        curr.erase(curr.begin(),curr.end());
        for(int i = 0; i<nums2.size();i++){
            if (visited1.find(nums2[i]) == visited1.end()){
                visited1.insert(nums2[i]);
                curr.push_back(nums2[i]);
            }
        }
        ret.push_back(curr);
        return ret;
    }
};