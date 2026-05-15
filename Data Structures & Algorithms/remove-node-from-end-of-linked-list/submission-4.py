# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return
        l = dummy = ListNode(0, head)
        r = head
        for i in range(n, 0, -1):
            prev, r = r, r.next
        
        while r:
            l, r = l.next, r.next
        
        l.next = l.next.next
        return dummy.next

        


        

        
        

        
        
        
