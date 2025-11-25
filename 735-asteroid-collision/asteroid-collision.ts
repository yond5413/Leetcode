function asteroidCollision(asteroids: number[]): number[] {
    const stack: number[] = [];
    
    for (const ast of asteroids) {
        let survived = true;
        
        while (stack.length > 0 && stack[stack.length - 1] > 0 && ast < 0) {
            const top = stack[stack.length - 1];
            if (top < -ast) {
                stack.pop(); // top destroyed, continue checking
                continue;
            } else if (top === -ast) {
                stack.pop(); // both destroyed
            }
            // if top > -ast or equal, current asteroid is destroyed
            survived = false;
            break;
        }
        
        if (survived) {
            stack.push(ast);
        }
    }
    
    return stack;
}