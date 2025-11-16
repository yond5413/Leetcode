function maxVowels(s: string, k: number): number {
    let hashmap = new Map<string,number>()
    hashmap.set("a",0)
    hashmap.set("e",0)
    hashmap.set("i",0)
    hashmap.set("o",0)
    hashmap.set("u",0)
    let ret = 0
    let count = 0
    let l = 0
    for (let r = 0;r<s.length;r++){
        if (hashmap.has(s[r].toLowerCase()) ){
            hashmap.set(s[r].toLowerCase(),hashmap.get(s[r].toLowerCase())+1)
            count++;
        }
        if (r-l+1 ==k){
            ret = Math.max(ret,count)
            if (hashmap.has(s[l].toLowerCase())){
                hashmap.set(s[l].toLowerCase(),hashmap.get(s[l].toLowerCase())-1) 
                count--
            }
            l++
        }
    }
    return ret
};