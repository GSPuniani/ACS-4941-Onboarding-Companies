"""
Problem:
Given a binary search tree, convert it into a sorted doubly-linked list 
by modifying the original tree nodes (do not create new nodes).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convertTree(self, root: Optional[TreeNode]) -> Optional[ListNode]:
        # Return nothing if input BST is empty
        if not root: 
            return

        # Use recursion
        if root.left:
            # Find in-order predecessor
            node = root.left
            while node.right:
                node = node.right
            # Restructure tree
            temp, root.left, node.right = root.left, None, root
            return self.convertTree(temp)
        # Assign pointers
        root.next = self.convertTree(root.right)
        if root.next: root.next.prev = root
        return root