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

function dfs(curr:TreeNode|null,leaves:number[]):TreeNode|null{
    if(curr == null){
        return null;
    }
    if(curr.left == null && curr.right== null){
        leaves.push(curr.val)
    }
    dfs(curr.left,leaves)
    dfs(curr.right,leaves)
}
////
function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    let r1:number[] = []
    let r2:number[] = []
    dfs(root1,r1)
    dfs(root2,r2)
    if (r1.length != r2.length ) return false;

    let n = r1.length
    for(let i = 0;i<n;i++){
        if (r1[i] != r2[i]){
            return false
        }
    }
    return true
};