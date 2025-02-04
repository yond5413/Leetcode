class Solution {
public:
    string decodeString(string s) {
        stack<char> st;
        for(int i = 0; i< s.size(); i++){
            if(s[i] == ']'){
                string decode = "";
                while(st.top() != '['){
                    decode = st.top()+decode;
                    st.pop();
                }
                st.pop(); // -> '['
                int num = 0;
                int base = 1;
                while(!st.empty() && isdigit(st.top())){
                    num = num+(st.top()-'0')*base;
                    st.pop();
                    base*=10;
                }
                while(num!=0){
                    for(int j = 0; j<decode.size();j++){
                        st.push(decode[j]);
                    }
                    num --;
                }
            }
            else{
                st.push(s[i]);
            }
        }
        ///////////////
        string ret = "";
       while(!st.empty()){
            ret = st.top() + ret;
            st.pop();
       }
        
        return ret;
    }
};