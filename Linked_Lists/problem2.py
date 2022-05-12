"""
Problem:
Given a singly-linked list, rearrange the nodes by interleaving the 
first half of the linked list with the second half.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Iterate with fast pointer and slow pointer to reach end and middle
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next
            
        # Reverse the second half of the list
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # Stitch together the first half and reversed second half
        fast_front = head
        while fast.next:
            tmp1 = fast_front.next
            tmp2 = fast.next
            fast_front.next = fast
            fast.next = tmp1
            fast_front = tmp1
            fast = tmp2