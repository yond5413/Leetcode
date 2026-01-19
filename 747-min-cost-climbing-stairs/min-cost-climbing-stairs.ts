function minCostClimbingStairs(cost: number[]): number {
    const n = cost.length
    let dp: number[] = Array(n).fill(0)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for (let i =2;i<n;i++){
        dp[i] = cost[i] + Math.min(dp[i-1],dp[i-2])
    }
    return Math.min(dp[n-2],dp[n-1])
};