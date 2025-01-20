#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(),piles.end());
        while(l<r){
            int k = (r+l)/2;
            int curr_time = 0;
            for (int i = 0; i<piles.size();i++){
                curr_time += ceil(piles[i]*1.0/k);
            }
            //////////////////////////////////////
            if (curr_time<=h){
                r = k;
            }
            else{
                l = k+1;
            }
        }
        return l;
    }
};