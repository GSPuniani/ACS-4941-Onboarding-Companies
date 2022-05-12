"""
Problem:
Given an array of k singly-linked lists, each of whose values are in sorted order, 
combine all nodes (do not create new nodes) into one singly-linked list with all values in order.
"""

# Not sure how to do this without creating new nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Return empty node if list is empty or contains only None
        if lists == [] or (len(lists) == 1 and lists[0] == None):
            return ListNode('', None)
        
        # Traverse the linked lists and add each value to a list
        n = 0
        lst = []
        for n in lists:
            while n != None:
                lst.append(n.val)
                n = n.next
        
        # If list exists, sort it and assign first element to head
        if lst:
            lst.sort()
            prev, cur = ListNode(lst[0], None), None
            head = prev
        else:
            return ListNode('', None)
        
        # Add sorted elements from list to return linked list
        for t in lst[1:]:
            cur = ListNode(t, None)
            prev.next = cur
            prev = prev.next
            
        return head
        