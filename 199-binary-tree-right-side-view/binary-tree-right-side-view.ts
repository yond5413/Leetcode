/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function rightSideView(root: TreeNode | null): number[] {
    if (root === null){
        return []
    }
    let ret = []
    let queue = [root]
    /*
    stack -> push,pop
    queue -> unshift,shift
    */
    while (queue.length>0){
        let n = queue.length
        for (let i =0;i<n;i++){
            let curr = queue.shift()
            if (i==0){
                ret.push(curr.val)
            }
            if (curr.right != null){
                queue.push(curr.right)
            }
             if (curr.left != null){
                queue.push(curr.left)
            }
        }
    }
    return ret;
};