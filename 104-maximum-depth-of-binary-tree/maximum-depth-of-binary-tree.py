# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr,tot):
            if not curr:
                return tot
            return max(dfs(curr.left,tot+1),dfs(curr.right,tot+1))
        return dfs(root,0)