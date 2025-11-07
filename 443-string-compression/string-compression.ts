function compress(chars: string[]): number {
    let l = 0
    let r = 0
    while (r<chars.length){
        let curr = chars[r]
        let count = 0
        while ( r<chars.length && curr == chars[r]){
            r++
            count++
        }
        chars[l] = curr
        l++
        if (count >1){
            let digits = count.toString()
            for (let i = 0;i<digits.length;i++){
                chars[l] = digits[i]
                l++ 
            }
        }
    }
    return l;
};