# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(curr,level):
            
            if not curr.left and not curr.right:
                return level+1
            elif not curr.left:
                return dfs(curr.right,level+1)
            elif not curr.right:
                return dfs(curr.left,level+1)
            return min(dfs(curr.left,level+1),dfs(curr.right,level+1))
        return dfs(root,0)