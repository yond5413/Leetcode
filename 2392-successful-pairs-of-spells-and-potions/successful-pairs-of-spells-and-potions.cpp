#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int n = spells.size(), m = potions.size();
        vector<int> ret(n);
        sort(potions.begin(),potions.end());
        for (int i = 0; i<n;i++){
            int l = 0, r = m-1;
            while(l<=r){
             int mid = l+(r-l)/2;
                if ((static_cast<long long>(spells[i])*static_cast<long long>(potions[mid]))>=success){
                    r = mid-1;
                 }
                else{
                    l = mid+1;
             }  
            }
            ret[i] = m-l;
        }
        return ret;
    }
};