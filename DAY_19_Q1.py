# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head
        curr = head
        Next = curr

        while(curr):
            Next = Next.next
            curr.next = prev
            prev = curr
            curr = Next
        
        head.next = None
        return prev
