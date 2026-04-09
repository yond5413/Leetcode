function maxProfit(prices: number[]): number {
  let ret:number = 0 
    let l:number = 0
    for (let r = 1; l<prices.length; r++){
        if (prices[l] < prices[r]){
            ret = Math.max(ret,prices[r]-prices[l])
        }
        else{
            l = r
        }
    }    

    return ret 
};