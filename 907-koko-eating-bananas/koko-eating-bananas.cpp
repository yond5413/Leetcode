#include <algorithm>
#include <cmath>
class Solution {
public:
    int getTime(vector<int>& piles,int k){
        long ret = 0;
        for(int i = 0; i<piles.size();i++){
            ret += ceil(piles[i]*1.0/k);
        }
        return static_cast<int>(ret);
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1; 
        int r = *max_element(piles.begin(),piles.end());
        while(l<r){
            int k = (l+r)/2;
            int curr_time = getTime(piles,k);
            if (curr_time <= h){
                r = k;
            }
            
            else{
                l = k+1;
            }
                
        }
        return l;
    }
};