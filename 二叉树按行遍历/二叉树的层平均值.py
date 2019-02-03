
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        outList = []
        queue = []
        if root is None :
            return outList
        else:
            queue.append(root)
        while queue:
            nextQueue = []
            s = 0
            for point in queue:
                s = s +point.val
                if point.left is not None:
                    nextQueue.append(point.left)
                if point.right is not None:
                    nextQueue.append(point.right)
            res = s/len(queue)
            outList.append(res)
            queue = nextQueue
        return outList