class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> r_queue;
        queue<int>d_queue;
        int n = senate.size();
        ///////////////////////
        for(int i = 0; i<n;i++){
            if (senate[i] =='R'){
                r_queue.push(i);
            }
            else{
                d_queue.push(i);
            }
        }
        ///////////////////////
        while(!d_queue.empty() && !r_queue.empty()){
            int r =r_queue.front();
            r_queue.pop();
            int d = d_queue.front();
            d_queue.pop();
            if (d<r){
                d_queue.push(d+n);
            }
            else{
                r_queue.push(r+n);
            }
        }
        return d_queue.empty() ? "Radiant": "Dire";
    //
    }
};