function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    let n = candies.length 
    let ret = Array(n).fill(false);
    let max = Math.max(...candies)// ... is spread operator?
    for (let i = 0;i<n;i++){
        if (candies[i]+extraCandies >= max){
            ret[i] = true
        }
    }  
    return ret
};