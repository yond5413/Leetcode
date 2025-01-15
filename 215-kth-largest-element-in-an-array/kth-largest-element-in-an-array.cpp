#include <iostream>
#include <queue>
class Solution {

public:
    int findKthLargest(vector<int>& nums, int k) {
        std:: priority_queue<int> heap;
        std::cout << "hi";
        for (int i = 0; i<nums.size();i++){
            heap.push(-nums[i]);
            if (heap.size()>k){
                
                std::cout<< heap.top();
                heap.pop();
            }
        }
        return -heap.top();
    }
};