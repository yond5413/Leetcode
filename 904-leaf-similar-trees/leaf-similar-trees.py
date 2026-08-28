# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1,r2 = [],[]
        def dfs(curr,leaves):
            if not curr:
                return None
            if not curr.left and not curr.right:
                leaves.append(curr.val)
            dfs(curr.left,leaves)
            dfs(curr.right,leaves)
        dfs(root1,r1)
        dfs(root2,r2)
        return r1 == r2