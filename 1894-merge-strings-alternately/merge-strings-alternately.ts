function mergeAlternately(word1: string, word2: string): string {
    let ret = ""
    const n = Math.max(word1.length,word2.length)
    for (let k = 0; k <n; k++ ){
        if (k<word1.length) ret += word1[k]
        if (k<word2.length) ret += word2[k]
    }   
    return ret
};