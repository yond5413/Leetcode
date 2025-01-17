#include <iostream>
#include <map>
#include <vector>
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int ret = 0;
        map<vector<int>,int> lookup;
        int n = grid.size();
        ////////////////////////////
        for(int i = 0; i<n; i++){
            lookup[grid[i]]++;
        }
        ////////////////////////////
        for (int c = 0; c < n; c++){
            vector<int> col;
            for (int i = 0; i < n;i++){
                col.push_back(grid[i][c]);
            }
            ret += lookup[col];
        }
    return ret;
    }
};