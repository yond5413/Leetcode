#include <iostream>
#include <vector>
#include <queue>
#include<deque>
/////////////////////////////
class RecentCounter {
public:
    queue<int> q;

    RecentCounter() {
        std:: cout<< "lmao \n";
    }
    
    int ping(int t) {
     /*
      1<= t <= 10**4
        return requests in inclusive range:
        [t-3000,t]     
      */
        int lower =  t-3000;
        //vector<int> q;
        q.push(t);
        while(!q.empty() && q.front()<lower){
            q.pop();
        }
        return q.size();

    }

};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */