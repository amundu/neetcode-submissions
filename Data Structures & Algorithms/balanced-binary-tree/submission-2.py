# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.dfs(root)
        return self.is_balanced
        
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.is_balanced = abs(left-right) <= 1 if self.is_balanced else False

        return max(left, right)+1