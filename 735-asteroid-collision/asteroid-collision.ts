function asteroidCollision(asteroids: number[]): number[] {
    let ret:number[] = []
    for (const ast of asteroids){
        let flag = true
        while (ret.length && ret[ret.length-1]>0 && ast<0){
            let top =  ret[ret.length-1]
            if (top<-ast){
                ret.pop()
                 continue
            }
            else if(top===-ast){
                ret.pop()
            }
                flag = false
                break
            
        }
        if (flag){
            ret.push(ast)
        }
    }
    return ret
};