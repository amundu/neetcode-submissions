# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qp = deque([p])
        qq = deque([q])

        while qp and qq:
            for _ in range(len(qp)):
                p_node, q_node = qp.popleft(), qq.popleft()
                if not(p_node or q_node):
                    continue
                if (not p_node or not q_node) or p_node.val != q_node.val:
                    return False
                qp.append(p_node.left)
                qp.append(p_node.right)
                qq.append(q_node.left)
                qq.append(q_node.right)
        return True