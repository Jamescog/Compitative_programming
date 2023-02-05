"""
Question statement
==================================================================
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.
=====================================
Time complexity
=====================================
O(n)
=====================================
Space complexity
=====================================
O(1)
=====================================
Approach
=====================================
Linked-lists
=====================================
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node as the head of the final merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Iterate through both input linked lists while they both have nodes
        while list1 and list2:
            if list1.val < list2.val:
                # Append the node with a smaller value to the final list
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Append the remaining nodes of the non-exhausted input list to the final list
        curr.next = list1 if list1 else list2
        
        # Return the head of the final list
        return dummy.next
