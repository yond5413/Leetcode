# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root,0)]
        lookup = {}
        l,r = 0,0
        while queue:
            curr,level = queue.pop(0)
            if level not in lookup:
                lookup[level] = []
            lookup[level].append(curr.val)
            if curr.left:
                queue.append((curr.left,level-1))
                l = min(l,level-1)
            if curr.right:
                queue.append((curr.right,level+1))
                r = max(r,level+1)
            
        ret = []
        for i in range(l,r+1):
            ret.append(lookup[i])
        return ret