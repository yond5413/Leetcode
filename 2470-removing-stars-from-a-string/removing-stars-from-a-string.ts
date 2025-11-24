function removeStars(s: string): string {
    let stack = [];
    for (let ch of s){
        if (ch === "*"){
            stack.pop()
        }
        else{
            stack.push(ch)
        }
    }
    return stack.join("")
};