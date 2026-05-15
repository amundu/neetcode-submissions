# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second = head
        for i in range(n):
            second = second.next
        prev = None
        first = head
        while second:
            prev = first
            first, second = first.next, second.next
        
        if prev == None:
            if first.next:
                return first.next
            return None
        
        prev.next = first.next
        return head