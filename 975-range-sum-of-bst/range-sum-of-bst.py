# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ret = 0
        if not root:
            return ret
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.val >=low and curr.val<=high:
                ret+=curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return ret
