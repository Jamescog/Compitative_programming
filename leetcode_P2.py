"""
Question Statement
==================================================================
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
===================================================================
Time complexity
====================================================================
O(max(m, n))
 where m and n are the lengths of the linked lists l1 and l2, respectively.
This is because the while loop continues until both linked lists are processed and 
here is no more carry, which takes at most max(m, n) iterations.
====================================================================
Space Complexity
====================================================================
O(max(m,n))
This is because in the worst case scenario, each digit in both linked lists
requires a new node to be created in the result linked list.
====================================================================
Approach
====================================================================
Linked-lists
===================================================================
"""


from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # create a dummy node
        curr = dummy  # set current node as dummy node
        carry = 0  # initialize carry

        # continue while either l1 or l2 has nodes, or carry is not zero
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # get value of l1 node or 0 if not available
            val2 = l2.val if l2 else 0  # get value of l2 node or 0 if not available
            carry, val = divmod(val1 + val2 + carry, 10)  # get the carry and digit
            curr.next = ListNode(val)  # add the digit to the linked list
            curr = curr.next  # move to the next node
            l1 = l1.next if l1 else None  # move to the next node of l1 if available
            l2 = l2.next if l2 else None  # move to the next node of l2 if available

        return dummy.next  # return the next node after the dummy node
