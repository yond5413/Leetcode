function reverseWords(s: string): string {
    let curr = s.split(" ").filter(word => word!="")
    console.log(curr);
    let l = 0;
    let r = curr.length -1;
    while (l<=r){
        let temp = curr[l]
        curr[l] = curr[r]
        curr[r] = temp
        l++
        r--
    }
    return curr.join(" ")
};