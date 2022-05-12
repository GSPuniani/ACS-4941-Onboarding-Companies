"""
Problem:
Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Return head if empty or k is 0
        if not head or not head.next or k == 0:
            return head
        
        # Keep count from traversal
        count = 1
        p = head
        while p.next:
            count += 1
            p = p.next
        p.next = head
        # Modify k based on number of full cycles
        k = count - (k % count)
        
        while k > 0:
            k -= 1
            p = p.next
        head = p.next
        p.next = None
        
        return head
        