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
function dfs(curr:TreeNode|null, count:number){
    if (curr === null){
        return count
        }
    return Math.max(dfs(curr.left,count+1),dfs(curr.right,count+1))
}
function maxDepth(root: TreeNode | null): number {
    return dfs(root,0)
};
