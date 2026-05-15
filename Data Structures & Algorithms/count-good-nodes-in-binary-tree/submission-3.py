# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: Optional[TreeNode], max_val: int) -> int:
            if not root:
                return 0
            res = 1 if root.val >= max_val else 0
            new_max_val = max(max_val, root.val)
            res += dfs(root.left, new_max_val)
            res += dfs(root.right, new_max_val)
            return res
        return dfs(root, float('-inf'))