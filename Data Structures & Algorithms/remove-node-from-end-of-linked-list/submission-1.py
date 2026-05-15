# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return
            curr, prev = head, None
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            print(prev.val)
            return prev
        
        head = reverse(head)
        curr = head
        prev = None
        for i in range(n, 1, -1):
            prev, curr = curr, curr.next
        if prev == None:
            head = head.next
        else:
            prev.next = curr.next
        head = reverse(head)
        return head

        
        
        
