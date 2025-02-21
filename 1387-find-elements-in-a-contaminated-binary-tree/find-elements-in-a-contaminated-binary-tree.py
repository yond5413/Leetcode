# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lookup = set()
        self.clean_up()
        
    def clean_up(self):        
        if self.root:
            self.root.val = 0
            queue = [self.root]
            while(queue):
                curr = queue.pop()
                self.lookup.add(curr.val)
                if curr.left:
                    curr.left.val =2*curr.val +1
                    queue.append(curr.left)
                if curr.right:
                    curr.right.val =2*curr.val +2
                    queue.append(curr.right)
                ###################################
    def find(self, target: int) -> bool:
        return target in self.lookup

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)