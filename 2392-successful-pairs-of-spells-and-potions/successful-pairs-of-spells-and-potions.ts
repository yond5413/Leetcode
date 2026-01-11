function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    let n = spells.length
    let m = potions.length
    let ret = []
    potions.sort((a,b)=>a-b)
    for (let i = 0; i<n;i++){
        let l = 0
        let r = m-1
        while(l<=r){
            let j = Math.floor((l+r)/2)
            if (spells[i]*potions[j]>=success){
                r = j-1
            }
            else{
                l = j+1
            }
        }
        ret.push(m-l)

    }
    return ret
};