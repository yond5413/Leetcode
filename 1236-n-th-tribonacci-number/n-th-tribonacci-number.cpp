#include <iostream>
#include <vector>
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0){
            return 0;
        }
        if (n == 1 ||  n == 2){
            return 1;
        }
    vector<int> fib(n+1); 
    fib[1] = 1;
    fib[2] = 1;
        for (int i = 3;i<n+1; i++){
            fib[i] = fib[i-1]+fib[i-2]+fib[i-3];
        }
    return fib[n];
    }
};