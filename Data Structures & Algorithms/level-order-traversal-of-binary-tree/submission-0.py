# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            nodes_in_level = []
            while q:
                nodes_in_level.append(q.popleft())
            for node in nodes_in_level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append([n.val for n in nodes_in_level])
        return res
        