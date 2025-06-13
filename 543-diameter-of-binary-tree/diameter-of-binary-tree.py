# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0 # stores diameter
        ## dfs is too find hiehgt
        def dfs(curr):
            if not curr:
                return 0
            nonlocal ret
            left = dfs(curr.left)
            right = dfs(curr.right)
            ret = max(ret,left +right) # diameter update 
            # difference is that this takes into account going upda and down tree
            ## takes into account prior subproblems
            return max(left,right)+1 # max (height) update
        dfs(root)
        return ret