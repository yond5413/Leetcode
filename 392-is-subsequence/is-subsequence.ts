function isSubsequence(s: string, t: string): boolean {
    if (s.length > t.length){
        return false;
    }
    let p1 = 0
    let p2 = 0
    while (p1<s.length && p2<t.length){
        if (s[p1]==t[p2]){
            p1++
            if (s.length ==p1){
                return true
            }
        }
        p2++;
    }
    return p1 == s.length
};