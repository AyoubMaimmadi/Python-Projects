class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left - left 
        self.right - right 

class Solution:
    def inverseTree(self, root: TreeNode) -> TreeNode:

        if not root: 
            return None

        #swap children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.inverseTree(root.left)
        self.inverseTree(root.right)
        return root
