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
        created = defaultdict(lambda: Node(0))

        curr = head
        temp = dummy = Node(0)
        i = 0
        while curr:
            new_node = created[curr]
            random_node = created[curr.random] if curr.random else None
            new_node.val, new_node.random = curr.val, random_node
            temp.next = new_node
            temp, curr = temp.next, curr.next
            i += 1
        return dummy.next
        