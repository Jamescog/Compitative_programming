"""
Question Statements
================================================
Given the head of a linked list, remove the nth node from the end of the list and return its head.
=================================================
Time complexity
================================================
O(n)
================================================
Space complexity
================================================
O(1)
================================================
Approach
===============================================
Two-Pointers
===============================================
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head

        # initialize two pointers, first and second, both pointing to the dummy node
        first = dummy
        second = dummy

        # move the second pointer n nodes ahead of the first pointer
        for i in range(n):
            second = second.next

        # move both pointers together until the second pointer reaches the end of the list
        while second.next:
            first = first.next
            second = second.next

        # first pointer is now pointing to the node that needs to be removed
        # remove the node by updating the next pointer of the previous node to skip over the node to be removed
        first.next = first.next.next

        # return the head of the list
        return dummy.next
