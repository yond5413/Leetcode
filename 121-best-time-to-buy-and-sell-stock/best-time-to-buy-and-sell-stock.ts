function maxProfit(prices: number[]): number {
    let ret = 0
    let l = prices[0]
    for (let r= 1; r<prices.length; r++){
        ret = Math.max(ret,prices[r]-l )
        l = Math.min(l,prices[r])
    }
    return ret
};