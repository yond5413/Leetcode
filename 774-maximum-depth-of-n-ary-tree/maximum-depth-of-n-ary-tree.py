"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(curr,tot):
            if not curr or not curr.children:
                return tot
            ret = 0

            for c in curr.children:
                ret = max(ret,dfs(c,tot+1))
            return ret
        return dfs(root,1)