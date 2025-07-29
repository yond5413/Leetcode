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
            return None
        queue = [node]
        lookup = {} #val: node clone as pair
        while queue:
            curr = queue.pop()
            if curr.val not in lookup:
                lookup[curr.val] = Node(val=curr.val)
                for vert in curr.neighbors:
                    if vert.val in lookup:
                        lookup[curr.val].neighbors.append(lookup[vert.val])
                    else:
                        lookup[vert.val] = Node(vert.val)
                        queue.append(vert)
                        lookup[curr.val].neighbors.append(lookup[vert.val])
            elif len(curr.neighbors) !=  len(lookup[curr.val].neighbors):
                for vert in curr.neighbors:
                    if vert.val in lookup:
                        lookup[curr.val].neighbors.append(lookup[vert.val])
                    else:
                        lookup[vert.val] = Node(vert.val)
                        queue.append(vert)
                        lookup[curr.val].neighbors.append(lookup[vert.val])
        return lookup[node.val]
        