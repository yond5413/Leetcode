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

function sumRootToLeaf(root: TreeNode | null): number {
    let dfs = (curr:TreeNode,val:String)=>{
        if (curr === null){
            return 0;
        }
        if (curr.left === null && curr.right === null){
            const bin = String(val)+curr.val
            let ret = parseInt(bin,2)
            return ret
        }
        return dfs(curr.left,String(val)+curr.val) +dfs(curr.right,String(val)+curr.val)
    }
    return dfs(root,"")
};