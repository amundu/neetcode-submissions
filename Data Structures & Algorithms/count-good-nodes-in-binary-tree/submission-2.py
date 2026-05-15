# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: Optional[TreeNode], max_n: int) -> int:
            if not root:
                return 0
            new_max_n = max(max_n, root.val)
            children = helper(root.left, new_max_n) + helper(root.right, new_max_n)
            return children + int(root.val == new_max_n)
        return helper(root, float('-inf'))