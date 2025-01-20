#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(),piles.end());
        int ret = r;
        while(l<=r){
            int k = (r+l)/2;
            long long curr_time = 0;
        
            for (int i = 0; i<piles.size();i++){
                curr_time += ceil(static_cast<double>(piles[i])/k);
            }
            //////////////////////////////////////
            if (curr_time<=h){
                ret = k;
                r = k-1;
                
            }
            else{
                l = k+1;
            }
        }
        return ret;
    }
};