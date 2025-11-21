function closeStrings(word1: string, word2: string): boolean {
    if (word1.length !=word2.length){
       return false 
    }
    let lookup1 = new Map()
    let lookup2 = new Map()
    for (let i = 0;i<word1.length;i++){
        lookup1.set(word1[i],(lookup1.get(word1[i]) ?? 0)+1)
        lookup2.set(word2[i],(lookup2.get(word2[i]) ?? 0)+1)
    }
    //
    let freq1 = new Map()
    let freq2 = new Map()
    for (const val of lookup1.values()){
        freq1.set(val,(freq1.get(val)??0)+1)
    }
    for (const val of lookup2.values()){
        freq2.set(val,(freq2.get(val)??0)+1)
    }
    ///
    const set1 = new Set(lookup1.keys())
    const set2 = new Set(lookup2.keys())
    if (set1.size != set2.size || ![...set1].every(c=>set2.has(c))){
        return false
    }
    if (freq1.size !=freq2.size) return false;
    for (const [freq,count] of freq1){
        if(freq2.get(freq)!= count) return false;
    }
    return true
};