# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # True -> right
        # False -> left
        if not root:
            return 0
        def dfs(node,direction,total):
            if not node:
                return total
            if direction:
                l = dfs(node.left,False,total+1)
                r = dfs(node.right,True,1)
            else:
                l = dfs(node.left,False,1)
                r = dfs(node.right,True,total+1)
            return max(l,r)
        return dfs(root,None,0)-1