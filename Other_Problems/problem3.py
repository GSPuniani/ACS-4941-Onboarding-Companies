"""
Problem:
Let's say a binary tree is "super balanced" if the difference between the depths of any two leaf nodes is at most one. 
Write a function to check if a binary tree is "super balanced".
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return True if tree is empty
        if root is None: 
            return True
        
        # Helper function to calculate height
        def height(root):
            if root is None:
                return 0
            
            right_height = height(root.right)
            left_height = height(root.left)
            
            if left_height == -1 or right_height == -1:
                return -1
            if abs(right_height - left_height) > 1: 
                return -1
            
            return 1 + max(left_height, right_height)
            
            
        # -1 is the sentinel value for False
        return height(root) != -1