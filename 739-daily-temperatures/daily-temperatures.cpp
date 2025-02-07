#include <iostream>
#include <vector>
#include <stack>
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        std::cout << n << endl;
        vector<int> ret(n); 
        stack<int> st;
        for(int i = n-1; i>=0; i--){
            while( !st.empty() && temperatures[i]>=temperatures[st.top()]){
                st.pop();
            }
            if(!st.empty()){
                ret[i] = st.top()-i;
            }
            st.push(i);

            
        }
        return ret;
    }
};