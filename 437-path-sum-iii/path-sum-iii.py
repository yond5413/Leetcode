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
            count = 0
            if curr:
                total += curr.val
                count += lookup[total-targetSum] 
                lookup[total]+=1
                count += dfs(curr.left,total) + dfs(curr.right,total)
                lookup[total]-=1
            return count
        return dfs(root,0)