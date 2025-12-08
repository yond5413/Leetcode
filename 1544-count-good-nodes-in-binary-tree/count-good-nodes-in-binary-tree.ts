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
 function dfs(curr:TreeNode|null,max_val:number):number{
    if (curr === null){
        return 0
    }
    if (curr.val>=max_val){
        return dfs(curr.left,curr.val)+dfs(curr.right,curr.val)+1
    }
    else{
        return dfs(curr.left,max_val)+dfs(curr.right,max_val)
    }
 }

function goodNodes(root: TreeNode | null): number {
    return dfs(root,root.val)
};