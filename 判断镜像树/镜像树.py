'''
对称树：有左子树就要有右子树
镜像树：在对称的基础上，左右子树的值相同
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compare(self,l,r):
        if ~l or ~r:
            return ~l and ~r
        else:
            return l.val == r.val and self.compare(l.left,r.right) and self.compare(l.right,r.left)

    def sameTree(self, root):
        return ~root or self.compare(root.left,root.right)
