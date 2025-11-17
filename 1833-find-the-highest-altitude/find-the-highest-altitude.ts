function largestAltitude(gain: number[]): number {
    const n = gain.length;
    let prefix = new Array(n+1).fill(0);
    for (let i = 1;i<prefix.length;i++){
        prefix[i] = gain[i-1]+prefix[i-1]
    }
    return Math.max(...prefix);
};