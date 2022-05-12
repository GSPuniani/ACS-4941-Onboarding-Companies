"""
Problem:
Given a binary search tree, reverse the order of its values by modifying the nodes' links.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Return root if tree is empty
        if not root:
            return root
        
        # Use queue to track BFS traveral
        bfs_queue = [root]
        while bfs_queue:
            node = bfs_queue[-1]
            del bfs_queue[-1]
            
            if node.left:
                bfs_queue.append(node.left)
            
            if node.right:
                bfs_queue.append(node.right)
                
            # Swap left and right children
            node.left, node.right = node.right, node.left
        return root