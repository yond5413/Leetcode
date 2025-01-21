#include <cmath>
#include <iostream>
#include <vector>
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(),piles.end());
        
        while(l<=r){
            int k = r+(l-r)/2;
            long long time = 0;
            for(int i = 0; i< piles.size();i++){
                time +=ceil(static_cast<double>(piles[i])/k);
            }
            if(time>h){
                l = k+1;
            }
            else{
                r = k-1;
            }
        }
        return l;
    }
};