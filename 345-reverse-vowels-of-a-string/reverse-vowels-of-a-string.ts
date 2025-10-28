function reverseVowels(s: string): string {
    let curr = s.split("")
    const vowels = ["a","e","i","o","u"]
    let l = 0
    let r = s.length-1
    const lookup = new Set(vowels)
    while (l<r){
        if (lookup.has(s[l].toLowerCase()) && lookup.has(s[r].toLowerCase())) {
            curr[r] = s[l]
            curr[l] = s[r]
            l++;
            r--;
        }
        else if (lookup.has(s[l].toLowerCase()) ){
            r--;
        }
         else if (lookup.has(s[r].toLowerCase()) ){
            l++;
        }
        else{
            l++;
            r--;
        }
    }
    return curr.join("")
};