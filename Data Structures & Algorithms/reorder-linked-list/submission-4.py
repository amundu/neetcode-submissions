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
        second = slow.next
        prev = slow.next = None
        while second:
            second.next, prev, second = prev, second, second.next
        
        first, second = head, prev
        while second:
            first_tmp, second_tmp = first.next, second.next
            first.next, second.next = second, first_tmp
            first, second = first_tmp, second_tmp

