# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return 0
        
        def dfs(curr,closest):
            if not curr:
                return closest
            diff = abs(target-curr.val)
            if diff<abs(target-closest):
                closest = curr.val
            elif diff == abs(target-closest):
                closest =min(curr.val,closest)
            if curr.val>target:
                return dfs(curr.left,closest)
                #return min(closest,dfs(curr.left,closest))
            elif curr.val<target:
                #return #min(closest,dfs(curr.right,closest))
                return dfs(curr.right,closest)
            return closest

        return dfs(root,root.val)