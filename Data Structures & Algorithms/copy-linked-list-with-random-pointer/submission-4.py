"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        tmp = head
        orig_to_copy = {}
        while tmp:
            orig_to_copy[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        tmp = head
        while tmp:
            orig_to_copy[tmp].next = orig_to_copy[tmp.next] if tmp.next else None
            orig_to_copy[tmp].random = orig_to_copy[tmp.random] if tmp.random else None
            tmp = tmp.next
        return orig_to_copy[head]