/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    return valid(root, math.MinInt64, math.MaxInt64)
}

func valid(node *TreeNode, left, right int) bool {
    if node == nil {
        return true
    }

    if node.Val <= left || node.Val >= right {
        return false
    }

    return valid(node.Left, left, node.Val) && valid(node.Right, node.Val, right)
}