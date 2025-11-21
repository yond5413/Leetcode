function uniqueOccurrences(arr: number[]): boolean {
    let lookup = new Map()
    for(let i = 0;i<arr.length;i++){
        if (lookup.has(arr[i])){
            lookup.set(arr[i],lookup.get(arr[i])+1)
        }
        else{
            lookup.set(arr[i],1)
        }
    }
    ///
    let seen = new Set();
    for (const val of lookup.values()){
        if (seen.has(val)){
            return false;
        }
        else {
            seen.add(val)
        }
    }
    return true;
};