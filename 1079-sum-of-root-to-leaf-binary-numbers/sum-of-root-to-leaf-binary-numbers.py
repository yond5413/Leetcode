# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr,val):
            if not curr:
                return 0
            if not curr.left and not curr.right:
                return int(val+str(curr.val),2)
            return dfs(curr.left,val+str(curr.val))+dfs(curr.right,val+str(curr.val))
        return dfs(root,"")