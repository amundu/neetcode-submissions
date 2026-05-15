# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow.next
        slow.next = None
        slow = prev
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        tail = prev
        head_tmp = head
        while tail:
            head_next, tail_next = head_tmp.next, tail.next
            head_tmp.next, tail.next = tail, head_tmp.next
            head_tmp, tail = head_next, tail_next

