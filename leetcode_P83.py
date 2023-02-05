"""
Question Statement
================================================
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
================================================
Time complexity
================================================
O(n)
================================================
Space complexity
================================================
O(1)
================================================
 Approach
 ==============================================
 Linked-lists
 ==============================================
 """
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a pointer to traverse the input linked list
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the next node if its value is the same as the current node's
                curr.next = curr.next.next
            else:
                # Move to the next node if the values are different
                curr = curr.next
        return head
