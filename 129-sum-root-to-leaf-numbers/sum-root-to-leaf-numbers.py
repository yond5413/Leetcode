# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr,total):
            if not curr:
                return 0
            total +=curr.val
            if not curr.left and not curr.right:
                return total
            return dfs(curr.left,total*10) + dfs(curr.right,total*10)
        return dfs(root,0)