"""
Problem:
Given a binary search tree containing integers and a target integer, 
come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Use queue to track BFS traversal
        bfs_queue = [root]
        # Use a set to track difference values with O(1) look-up time
        bfs_set = set()
        # Iterate through queue, check for differences in set
        for node in bfs_queue:
            # If difference found, then two-sum is satisfied
            if abs(k - node.val) in bfs_set: 
                return True
            # Add the value to the set and its children to the queue
            bfs_set.add(node.val)
            if node.left: 
                bfs_queue.append(node.left)
            if node.right: 
                bfs_queue.append(node.right)
        # Return False is queue has been iterated over and no pairs found
        return False