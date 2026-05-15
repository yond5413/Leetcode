# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        ret = 0
        while stack:
            curr,level = stack.pop(0)
            if curr.left:
                stack.append((curr.left,level+1))
            if curr.right:
                stack.append((curr.right,level+1))
            ret = max(ret,level)
        return ret