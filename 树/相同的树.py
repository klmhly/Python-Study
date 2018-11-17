# 判断两棵二叉树是否相同
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 递归停止的条件
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            return l and r
        else:
            return False