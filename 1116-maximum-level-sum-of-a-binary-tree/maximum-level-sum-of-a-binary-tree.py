# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level_sum = {}
        queue = [(root,1)]
        while queue:
            curr,level = queue.pop(0)
            if level in level_sum:
                level_sum[level] +=curr.val
            else:
                level_sum[level] =curr.val
            if curr.left:
                queue.append((curr.left,level+1))
            if curr.right:
                queue.append((curr.right,level+1))
        ret,curr_max = 0,float("-inf")
        keys = list(level_sum.keys())
        for k in keys:
            if curr_max<level_sum[k]:
                ret = k
                curr_max = level_sum[k]
        return ret
