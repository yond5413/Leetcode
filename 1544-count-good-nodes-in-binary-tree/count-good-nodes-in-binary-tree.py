# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(curr,path_max):
            if not curr:
                return 0
            if curr.val>=path_max:
                path_max = curr.val
                return dfs(curr.left,path_max)+dfs(curr.right,path_max)+1
            else:
                return dfs(curr.left,path_max)+dfs(curr.right,path_max)
        return dfs(root,root.val)
       
