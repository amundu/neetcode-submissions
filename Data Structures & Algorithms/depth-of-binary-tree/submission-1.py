# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        max_depth = 1
        q.append((root, 1))
        while q:
            node, curr_depth = q.popleft()
            max_depth = max(max_depth, curr_depth)
            if node.left:
                q.append((node.left, curr_depth+1))
            if node.right:
                q.append((node.right, curr_depth+1))
            
        return max_depth


        