function maxArea(height: number[]): number {
    let l = 0
    let r = height.length -1;
    let ret = 0
    while (l<r){
        if (height[r]<height[l]){
            ret = Math.max(ret,(r-l)*height[r])
            r--;
        }
        else{
            ret = Math.max(ret,(r-l)*height[l])
            l++;
        }
    }

    return ret;

};