function gcdOfStrings(str1: string, str2: string): string {
    let m = str1.length 
    let n = str2.length
    let min_r =Math.min(m,n)
    for (let r = min_r; r>0; r-- ){
        if (m%r ===0 && n%r ===0){
            let curr = str1.slice(0,r)
            if (curr.repeat(Math.floor(m/r)) ==str1 && 
            curr.repeat(Math.floor(n/r)) == str2){
                return curr
            }
        }

    }
    return ""
};