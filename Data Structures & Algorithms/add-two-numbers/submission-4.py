# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        remainder = 0

        while l1 or l2:
            curr_sum = 0
            if l1 and l2:
                curr_sum = l1.val + l2.val + remainder
            elif l1:
                curr_sum = l1.val + remainder
            else:
                curr_sum = l2.val + remainder
            digit = curr_sum%10
            remainder = curr_sum//10
            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if remainder:
            head.next = ListNode(remainder)
        return dummy.next