function containsDuplicate(nums: number[]): boolean {
    let lookup = new Set()
    for(let i of nums){
        if(lookup.has(i)){
            return true
        }
        else{
            lookup.add(i)
        }
    }
    return false
};