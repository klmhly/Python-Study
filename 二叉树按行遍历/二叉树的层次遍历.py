'''
题目：给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        outList = []
        if root is None:
            return outList
        else:
            queue.append(root)
        while queue:
            res = []
            nextQueue = []
            for point in queue:
                res.append(point.val)
                if point.left is not None:
                    nextQueue.append(point.left)
                if point.right is not None:
                    nextQueue.append(point.right)
            outList.append(res)
            queue = nextQueue
        return outList
