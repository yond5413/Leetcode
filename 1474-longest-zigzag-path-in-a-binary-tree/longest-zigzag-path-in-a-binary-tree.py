# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(curr,direction,total):
            if not curr:
                return total
            if direction:
                l = dfs(curr.left,False,total+1)
                r = dfs(curr.right,True,1)
            else:
                l = dfs(curr.left,False,1)
                r = dfs(curr.right,True,total + 1)
            return max(l,r)
        return dfs(root,None,0)-1