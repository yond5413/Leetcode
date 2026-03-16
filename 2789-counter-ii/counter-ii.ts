type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let cur:number = init
    return {
        increment: ()=> {
            cur++
            return cur
        },
        decrement:()=>{
            cur--
            return cur
        },
        reset:()=>{
            cur= init
            return cur
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */