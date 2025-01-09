# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        basically as we go across each path we are keeping track of the amount of 
        times across each path the max increases
        '''
        def dfs(node,maximum):
            if not node:
                return 0
            if node.val>= maximum:
                return dfs(node.left,node.val)+dfs(node.right,node.val)+1
            else:
                return dfs(node.left,maximum)+dfs(node.right,maximum)
        return dfs(root,root.val)