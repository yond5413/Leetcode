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
            if curr == q or curr == p:
                return curr
            if (curr.left == q or curr.left ==p) and (curr.right == q or curr.right ==p):
                return curr
            l,r = dfs(curr.left),dfs(curr.right)
            if l and r:
                return curr
            return l if l else r
            
        return dfs(root)
