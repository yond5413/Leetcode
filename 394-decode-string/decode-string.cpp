#include <cctype>// -> isdigit(ch)
#include <stack>
#include <string>
class Solution {
public:
    string decodeString(string s) {
        string ret= "";
        stack<char> st;
        for (int i = 0; i<s.size();i++){
           if (s[i] ==']'){
            string decode = "";
            while( st.top()!='['){
                decode = st.top() + decode;
                st.pop();
            }
            st.pop(); // popped '['
                /// get num 
                int num = 0;
                int base = 1;
                while(!st.empty() && isdigit(st.top())){
                    num = num + (st.top()-'0')*base;
                    st.pop();
                    base *=10;
                }
                cout << num << '\n';
                cout << base << '\n';
                while(num!=0){
                    for(int j = 0 ; j<decode.size(); j++){
                        st.push(decode[j]);
                    }
                    num--;
                }
           }
           else{
            st.push(s[i]);
           }
        }
        ////////////////////////////
        while( !st.empty()){
            ret = st.top() + ret;
            st.pop();
        }
        return ret;
    }
};