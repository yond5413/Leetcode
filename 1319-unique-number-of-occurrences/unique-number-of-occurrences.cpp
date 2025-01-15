#include <iostream>
#include <set>
#include <map>
#include <set>
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int,int> hashmap;
        set<int> lookup;
        for (int i = 0; i<arr.size();i++){
            // find either iterator with key/val or iter the end
            if(hashmap.find(arr[i]) == hashmap.end()){
                hashmap[arr[i]] = 1;
            }
            else{
                hashmap[arr[i]]++;
            }
        }
        for (auto it = hashmap.begin(); it != hashmap.end();it++){
            lookup.insert(it->second);
        }
        return lookup.size() == hashmap.size();
    }
};