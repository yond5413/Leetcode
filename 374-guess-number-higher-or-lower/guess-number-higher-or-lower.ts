/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */


function guessNumber(n: number): number {
    let l =1
    let r = n
    while (l<=r){
        let mid = Math.floor((r+l)/2)
        let res = guess(mid)
        if (res == 0){
            return mid
        }
        else if (res == 1){
            l = mid+1
        }
        else{
            r = mid-1
        }
    }
};