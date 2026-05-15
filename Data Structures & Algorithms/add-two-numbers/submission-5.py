# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        remainder = 0

        while l1 or l2 or remainder:
            curr_sum = 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            curr_sum = v1 + v2 + remainder
            digit = curr_sum%10
            remainder = curr_sum//10
            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next