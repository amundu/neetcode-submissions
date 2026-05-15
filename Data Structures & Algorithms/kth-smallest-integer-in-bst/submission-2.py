# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: Optional[TreeNode]) -> List[int]:
            return dfs(root.left) + [root.val] + dfs(root.right) if root else []
        
        return dfs(root)[k-1]
        
