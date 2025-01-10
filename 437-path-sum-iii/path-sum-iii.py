# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        ret = 0
        lookup = defaultdict(int)
        lookup[0] = 1
        def dfs(curr,targ):
            count = 0
            if curr:
                targ += curr.val
                count = lookup[targ-targetSum]
                lookup[targ] +=1
                count += dfs(curr.left,targ)+dfs(curr.right,targ)
                lookup[targ]-=1 
            return count 
        ret = dfs(root,0)
        return ret
        
    


        