# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root,0)]
        lookup = defaultdict(list)
        l,r = 0,0
        while queue:
            curr,level = queue.pop(0)
            lookup[level].append(curr.val)
            if curr.left:
                queue.append((curr.left,level-1))
                l = min(level-1,l)
            if curr.right:
                queue.append((curr.right,level+1))
                r = max(level+1,r)
        ret = []
        for i in range(l,r+1):
            ret.append(lookup[i])
        return ret