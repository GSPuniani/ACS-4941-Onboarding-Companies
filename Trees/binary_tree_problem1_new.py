"""
Problem:
New: Given a binary tree, check whether it is a valid binary search tree (values in order).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Implement DFS with a stack
        stack = []
        left = None
        # Add left elements to stack
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            # Pop leftmost element
            root = stack.pop()
            # Return False if BST property is violated
            if left and left.val >= root.val:
                return False
            # Continue traversal 
            left = root
            root = root.right
        # Return True if BST property never violated
        return True