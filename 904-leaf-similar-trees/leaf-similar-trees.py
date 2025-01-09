# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return 
            dfs(root.left,leaf)
            dfs(root.right,leaf)
        r1,r2 = [],[]
        dfs(root1,r1)
        dfs(root2,r2)

        return r1 == r2