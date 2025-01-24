#include <string>
#include <iostream>
#include <stack> //?
class Solution {
public:
    string removeStars(string s) {
        string ret;
        stack<char> st;
        
        for(int i = 0; i<s.size();i++){
            if(s[i] == '*' && !st.empty()){
                    st.pop();
            }
            else{
                st.push(s[i]);
            }
        }
        while(!st.empty()){
            ret+= st.top();//.append(st.top());             
            // stack.top() vs queue.front()
            st.pop();
        }
        std::reverse(ret.begin(),ret.end());
        
        return ret;
    }
};