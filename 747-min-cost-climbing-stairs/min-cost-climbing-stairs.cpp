#include <vector>
#include <cmath>
#include <iostream>

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
       int n = cost.size();
       vector<int> dp(n);
       dp[0] = cost[0];
       dp[1] = cost[1];
       for (int i =2; i<n;i++){
            dp[i] = cost[i];
            if (dp[i-1]<=dp[i-2]){
                dp[i]+= dp[i-1];
            }
            else{
                dp[i]+= dp[i-2];
            }
       }
        if (dp[n-1]<dp[n-2]){
            return dp[n-1];
        }
        else{
            return dp[n-2];
        }
    }
};