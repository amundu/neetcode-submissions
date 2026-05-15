# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return

        head = curr = self.reverse(head)
        prev = None
        for i in range(n, 1, -1):
            prev, curr = curr, curr.next
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return self.reverse(head)
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return
            curr, prev = head, None
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        
        
        
