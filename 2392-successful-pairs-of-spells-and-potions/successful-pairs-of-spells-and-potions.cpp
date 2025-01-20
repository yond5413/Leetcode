#include  <algorithm>

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        // Assuming potions are sorted rn?
        vector<int> ret(spells.size());
        int n = spells.size(),  m = potions.size();
        /*
        Basically going to multiply
        */
        sort(potions.begin(),potions.end());
        for (int i = 0; i<n; i++){
            long long int power = spells[i];
                    int l = 0, r = m-1;
                    int mid;
                    while(l<=r){
                        mid = l+(r-l)/2;
                        long long prod = power*(long long int)potions[mid];
                        //cout << "i:"<< i<<" Prod: "<<prod<<"\n";                       
                        if( prod>= success){
                            r = mid - 1;
                        }
                        else{
                            l = mid + 1;
                        }
                    }
                    //ret.push_back(m-l);/////??????
                ret[i] = m-l;
            }
            return ret;
    }
};