/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int l = 1, r = n;
        
        while(l<=r){
            int mid = l+(r-l)/2; 
            //(l+r)/2;
            //r+(l-r)/2;
            // this helps with integer overflow 
            // only works for integers which is fine for bin_search
            std:: cout << l << " l " << r <<" r  " << mid << " mid \n";
            if (guess(mid) == 0){
                return mid;
            }
            else if (guess(mid) == 1){
                    l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return -1;
    }
};