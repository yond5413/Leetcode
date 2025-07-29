"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        lookup,queue = {node.val:Node(node.val)},[node]
        while queue:
            curr = queue.pop()
            clone = lookup[curr.val]
            if curr.neighbors:
                for v in curr.neighbors:
                    if v.val not in lookup:
                        lookup[v.val] = Node(v.val)
                        queue.append(v)
                    clone.neighbors.append(lookup[v.val])
        return lookup[node.val]