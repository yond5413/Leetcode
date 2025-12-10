# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr
            if curr.left and val<curr.val:
                stack.append(curr.left)
            elif curr.right and val>curr.val:
                stack.append(curr.right)
            else:
                return None