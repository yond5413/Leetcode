function reverseVowels(s: string): string {
  let curr = s.split("")
 
    let l = 0
    let r = s.length-1
    const letters = ["a","e","i","o","u"]
    const vowels =new  Set(letters);
    
    while(l<=r){
        if (vowels.has(s[l].toLowerCase())&& vowels.has(s[r].toLowerCase())){
            curr[l] = s[r]
            curr[r] = s[l]
            l++;
            r--;
        }
        else if (vowels.has(s[l].toLowerCase())){
            r--;
        }
        else if (vowels.has(s[r].toLowerCase())){
            l++;
        }
        else{
            l++;
            r--;
        }
    }


  return curr.join("")  
};