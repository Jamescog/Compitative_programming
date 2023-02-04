"""
Question Statement
===========================================================
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
===========================================================
Time complexity
===========================================================
O(n)
===========================================================
Space complexity
===========================================================
O(1)
===========================================================
Approach
============================================================
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, both pointing to the head of the linked list
        slow = fast = head
        
        # Move fast pointer through the list twice as fast as the slow pointer
        # Check that fast pointer is not None and that its next node is not None
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        
        # Return slow pointer, which will be pointing to the middle node
        return slow
