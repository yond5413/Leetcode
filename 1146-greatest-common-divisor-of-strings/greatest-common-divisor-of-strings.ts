function gcdOfStrings(str1: string, str2: string): string {
  const [m,n] = [str1.length, str2.length]
  const min_r = Math.min(m,n)
  for (let k = min_r; k>=0;k--){
    if ( m%k ==0 && n%k == 0){
        let curr = str1.slice(0,k)
        if (curr.repeat(Math.floor(m/k))==str1 && curr.repeat(Math.floor(n/k))==str2) {
            return curr
        }
    }
  }
  return ""
};