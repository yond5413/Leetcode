# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## probs bfs??
        if not root:
            return []
        ret = []
        queue = [root]
        while(queue):
            length = len(queue)
            for i in range(length):
                curr = queue.pop(0)
                if i == 0:
                    ret.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

        return ret