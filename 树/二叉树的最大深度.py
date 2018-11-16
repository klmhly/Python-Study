# 深度优先遍历，递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1
