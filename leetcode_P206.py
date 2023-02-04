"""
Question statement
========================================================
Given the head of a singly linked list, reverse the list, and return the reversed list.
=========================================================
Time complexity
=========================================================
O(n)
=========================================================
Space complexity
=========================================================
O(1)
=========================================================
Approach
=========================================================
Linked-lists
========================================================
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev pointer to None
        prev = None
        
        # Iterate through linked list and reverse the pointers for each node
        while head:
            # Store the next node
            next_node = head.next
            # Reverse the pointer for the current node
            head.next = prev
            # Move the prev pointer to the current node
            prev = head
            # Move the head pointer to the next node
            head = next_node
        
        # Return the prev pointer, which will be the new head of the reversed linked list
        return prev
