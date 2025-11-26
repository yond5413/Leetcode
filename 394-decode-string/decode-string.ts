function decodeString(s: string): string {
    let ret:string = ""
    let strStack:string[] = []
    let numStack:number[] = []
    let num:number = 0
    const isDigit = (c:string):boolean => c>="0" && c<="9";
    for (let ch of s){
        if (isDigit(ch)){
            num = num*10 + Number(ch)
        }
        else if(ch == "["){
            numStack.push(num)
            strStack.push(ret)
            ret = ""
            num = 0
        }
        else if(ch == "]"){
            let old_num = numStack.pop()
            let old_str = strStack.pop()
            ret = old_str+ret.repeat(old_num)
        }
        else{
            ret+=ch
        }
    }
    return ret
};