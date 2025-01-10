# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr):
            if not curr:
                return None
            if curr == p or curr == q:
                return curr
            left, right = dfs(curr.left),dfs(curr.right)
            if left and right:
                return curr
            return left if left else right
        return dfs(root)