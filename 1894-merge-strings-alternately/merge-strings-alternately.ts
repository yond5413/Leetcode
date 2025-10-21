//import Math;
function mergeAlternately(word1: string, word2: string): string {
    let ret = ""
    const n = Math.max(word1.length,word2.length)
    for(let i = 0; i<n;i++){
        if (i< word1.length){
            ret+= word1[i]
        }
        if (i< word2.length){
            ret+= word2[i]
        }
    }
    return ret
};