#include <iostream>
#include <queue>
class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> r_queue;
        queue<int> d_queue;
        int n = senate.size();
        for(int i = 0;i<n;i++){
            if (senate[i] == 'R'){
                r_queue.push(i);
            }
            else{
                d_queue.push(i);
            }
        }
        while(!r_queue.empty() && !d_queue.empty()){
            int r = r_queue.front();
            int d = d_queue.front();
            d_queue.pop();
            r_queue.pop();
            ///////////////////
            if (r<d){
                r_queue.push(r+n);
            }
            else{
                d_queue.push(d+n);
            }
        }
        return d_queue.empty() ? "Radiant" :"Dire";
    }
};