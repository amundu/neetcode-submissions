# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left node cannot surpass middle (parent)
        # right node cannot be less than middle (parent)
        def dfs(root: Optional[TreeNode], left_limit: float, right_limit: float) -> bool:
            if not root: return True
            if left_limit < root.val < right_limit:
                return dfs(root.left, left_limit, root.val) and dfs(root.right, root.val, right_limit)
            return False
        
        return dfs(root, float('-inf'), float('inf'))