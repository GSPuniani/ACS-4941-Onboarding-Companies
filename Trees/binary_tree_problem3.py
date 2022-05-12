"""
Problem:
Given a binary tree containing numbers, find the maximum sum path (the path that has the largest sum of node values). 
The path may start and end at any node in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = float("-inf")
        # Call helper function
        self.dfs_max(root)
        return self.globalMax
    
    def dfs_max(self, node):
        # Return 0 if node is empty
        if not node:
            return 0
        
        # Recursively pass in node children
        leftMax = self.dfs_max(node.left)
        rightMax = self.dfs_max(node.right)
        # Keep max value only if it's positive; negative numbers should be left out
        leftMax = max(leftMax, 0) 
        rightMax = max(rightMax, 0)
        # Calculate max sum for the node
        self.globalMax = max(self.globalMax, node.val + leftMax + rightMax) 
        # Return max sum
        return node.val + max(leftMax, rightMax) 