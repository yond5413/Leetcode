# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        queue = [(root,0,0)] # node,level, offset
        l,r = 0,0
        while queue:
            curr,level,offset = queue.pop(0)
            hashmap[offset].append((curr.val,level))
            if curr.left:
                queue.append((curr.left,level+1,offset-1))
                l = min(l,offset-1)
            if curr.right:
                queue.append((curr.right,level+1,offset+1))
                r = max(r,offset+1)
        ret = []
        for i in range(l,r+1):
            curr = hashmap[i]
            curr.sort(key = lambda x:(x[1],x[0]))
            ret.append([j[0] for j in curr])
        return ret


            