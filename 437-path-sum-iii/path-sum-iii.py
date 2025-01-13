# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        lookup = defaultdict(int)
        lookup[0] = 1
        def dfs(curr,total):
            ret = 0
            if curr:
                total+=curr.val
                ret += lookup[total-targetSum]
                lookup[total]+=1
                ret+= dfs(curr.left,total)+dfs(curr.right,total)
                lookup[total]-=1

            return ret
        return dfs(root,0)