# 题目：给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''
输入: 1->1->2
输出: 1->2
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next is not None:
            if cur.val != cur.next.val:
                cur = cur.next
            else:
                cur.next = cur.next.next

        return head