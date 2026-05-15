# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        self.dfs(root)
        return self.max_path_sum
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_path_sum = max(self.max_path_sum, root.val)
        left_sum = max(self.dfs(root.left), 0)
        right_sum = max(self.dfs(root.right), 0)
        curr_sum = root.val + left_sum + right_sum
        self.max_path_sum = max(self.max_path_sum, curr_sum)
        return max(root.val + left_sum, root.val + right_sum)


