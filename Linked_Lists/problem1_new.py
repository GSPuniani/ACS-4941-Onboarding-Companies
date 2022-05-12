"""
Problem:
New: Given a singly-linked list and an integer k, find the value in the kth-to-last node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Set slow and fast pointers to head node
        slow = fast = head
        
        # Move fast pointer over by n places
        while n > 0:
            fast = fast.next
            n -= 1
			
        # If n is size of linked list, remove head
        if fast == None:
            return head.next
        
        # Move fast and slow pointers by 1 
        # Use fast and slow difference to locate target
        while fast:
            # Reassign slow's next pointer to delete target
            if fast.next == None:
                slow.next = slow.next.next
                return head
            fast = fast.next
            slow = slow.next