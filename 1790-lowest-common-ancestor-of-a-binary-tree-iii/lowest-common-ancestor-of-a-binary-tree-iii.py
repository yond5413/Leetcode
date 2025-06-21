"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    
        p_seen = set()
        a = p
        while a.parent:
            p_seen.add(a.val)
            a = a.parent
        b = q
        while b.parent:
            if b.val in p_seen:
                return b
            b = b.parent
        return b
        '''
        p_seen = set()
        a = p
        while a.parent:
            p_seen.add(a.val)
            a = a.parent
        b = q
        while b.parent:
            if b.val in p_seen:
                return b
            b = b.parent
        return b'''