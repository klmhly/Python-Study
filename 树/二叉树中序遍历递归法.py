class treeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        # 递归出口
        if root is None:
            return tree

        tree += self.inorderTraversal(root.left)
        tree.append(root.val)
        tree += self.inorderTraversal(root.right)
        return tree


# 测试
t1 = treeNode(1)
t1.right = t2 = treeNode(2)
t2.left = t3 = treeNode(3)
test = Solution()
res = test.inorderTraversal(t1)
print(res)