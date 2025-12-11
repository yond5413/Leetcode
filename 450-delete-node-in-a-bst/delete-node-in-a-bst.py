# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<key:
            root.right = self.deleteNode(root.right,key)
        elif root.val>key:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left and root.right:
                curr = root.right
                # get minimum from right side
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right,root.val)
            else:
                root = root.left if root.left else root.right
            
        return root