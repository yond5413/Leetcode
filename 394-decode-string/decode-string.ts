function decodeString(s: string): string {
    let ret:string = ""
    let num_stack:number[] = []
    let str_stack:string[] = []
    let num:number = 0
    const isDigit = (ch:string):boolean => ch>="0" && ch<="9";
    for (let ch of s){
        if (isDigit(ch)){
            num = num*10 + Number(ch)
        }
        else if(ch === "["){
            str_stack.push(ret)
            num_stack.push(num)
            num = 0
            ret = ""
        }
        else if(ch === "]"){
            let old_str = str_stack.pop()
            let old_num = num_stack.pop()
            ret = old_str + ret.repeat(old_num)
        }
        else{
            ret += ch
        }
    }
    return ret
};