class RecentCounter {
    constructor(private queue:number[] = []) {
        
    }
    ping(t: number): number {
        let lower = t-3000
        this.queue.push(t)
        while (this.queue[0]<lower){
            this.queue.shift()
        }
        return this.queue.length
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */