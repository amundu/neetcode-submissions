# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        output = 0
        while q:
            for i in range(len(q)):
                node, max_val = q.popleft()
                if node:
                    output += int(node.val >= max_val)
                    q.append((node.left, max(node.val, max_val)))
                    q.append((node.right, max(node.val, max_val)))
        return output