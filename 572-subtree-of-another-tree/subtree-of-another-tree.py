# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val and sameTree(p.left,q.left) and sameTree(p.right,q.right))
        def dfs(curr):
            if not curr:
                return False
            if sameTree(curr,subRoot):
                return True
            return dfs(curr.left) or dfs(curr.right)
        return dfs(root)