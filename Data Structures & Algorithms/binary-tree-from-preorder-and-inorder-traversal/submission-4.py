# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        curr = TreeNode(preorder[0])
        # No left side
        print(curr.val, preorder, inorder)
        if curr.val == inorder[0]:
            curr.right = self.buildTree(preorder[1:], inorder[1:])
        # No right side:
        elif curr.val == inorder[-1]:
            curr.left = self.buildTree(preorder[1:], inorder[:-1])
        # The tree has both parts
        else:
            inorder_root_idx = inorder.index(curr.val)
            pre_order_partition_idx = max(preorder.index(inorder[0]), preorder.index(inorder[inorder_root_idx-1]))+1
            curr.left = self.buildTree(preorder[1: pre_order_partition_idx],inorder[:inorder_root_idx])
            curr.right = self.buildTree(preorder[pre_order_partition_idx:],inorder[inorder_root_idx+1:])
        return curr
